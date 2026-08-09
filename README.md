# rmcm - remove (python) comments

this is a simple script to remove comments and docstrings from python files.

I (well mainly claude) made this after I spent too much time removing coments from the code I had to turn in for my classes.

## Installation

### NixOS

#### Add rmcm as a flake input

In your system flake's `flake.nix`, add rmcm to `inputs`:

```nix
inputs = {
  nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  rmcm.url = "github:thecosmomancer/rmcm";
  ...
};
```

#### Import the module in your NixOS configuration

Pass `rmcm` through to your modules (e.g. via `specialArgs` if using
flakes directly, or however your setup threads flake inputs to modules),
then import it alongside your other modules:

```nix
outputs = { self, nixpkgs, ... }@inputs: {
  nixosConfigurations.yourhostname = nixpkgs.lib.nixosSystem {
    system = "x86_64-linux";
    modules = [
      ./configuration.nix
      inputs.rmcm.nixosModules.default
      # ...your other modules
    ];
  };
};
```

#### Add the package in your system configuration

Add it to your system packages inside ```environment.systemPackages``` or to your user packages using [home-manager](https://github.com/nix-community/home-manager) by adding it inside of ```home.packages```.

### Other distros

#### Clone the repo

```bash
git clone https://github.com/thecosmomancer/rmcm.git
cd rmcm
```

##### Install python3

##### Run the setup script

```bash
./setup.sh
```

##### If the setup script is not executable

```bash
bash setup.sh
```
## Usage

```bash
rmcm -i {input_file} -o {output_file}
```

or to overwrite the input file:

```bash
rmcm -Oi {input_file}
```

the `-p` argument can be used to print the output to stdout.

## License

[MIT.](https://choosealicense.com/licenses/mit/) I hate long licensing texts.