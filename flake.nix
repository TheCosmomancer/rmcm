{
  description = "rmcm - remove comments from python files";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs, ... }:
    let
      systems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];
      forAllSystems = f: nixpkgs.lib.genAttrs systems (system: f system);
    in
    {
      packages = forAllSystems (system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
        in
        {
          rmcm = pkgs.writers.writePython3Bin "rmcm" { 
                flakeIgnore = [ "E501" "E265" ]; 
            } (
            builtins.readFile ./rmcm.py
          );
          default = self.packages.${system}.rmcm;
        }
      );

      overlays.default = final: prev: {
        rmcm = self.packages.${final.system}.rmcm;
      };

      nixosModules.default = { config, pkgs, ... }: {
        nixpkgs.overlays = [ self.overlays.default ];
      };

      apps = forAllSystems (system: {
        rmcm = {
          type = "app";
          program = "${self.packages.${system}.rmcm}/bin/rmcm";
        };
        default = self.apps.${system}.rmcm;
      });
    };
}
