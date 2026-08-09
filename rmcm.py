#! /usr/bin/env python3

def remove_comments_and_docstrings(source):

    def not_inlist(last_significant_token):

        if last_significant_token in (',', '[', '(', '{'):
            return False
        return True

    import io
    import tokenize

    io_obj = io.StringIO(source)
    out_tokens = []

    IGNORED_TOKENS = (
        tokenize.INDENT,
        tokenize.DEDENT,
        tokenize.NEWLINE,
        tokenize.NL,
        tokenize.COMMENT,
        tokenize.ENCODING,
    )
    last_significant_token = ''

    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0

    tokens = tokenize.generate_tokens(io_obj.readline)

    for tok in tokens:
        token_type, token_string, start, end, line = tok
        start_line, start_col = start
        end_line, end_col = end

        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            out_tokens.append(" " * (start_col - last_col))

        if token_type == tokenize.COMMENT:
            pass
        elif token_type == tokenize.STRING and prev_toktype in (tokenize.INDENT, tokenize.NEWLINE, tokenize.NL):
            stripped_line = line.strip()
            if stripped_line.startswith(("'''", '"""')) and stripped_line.endswith(("'''", '"""')) and not_inlist(last_significant_token):
                out_tokens.append("")
            else:
                out_tokens.append(token_string)
        else:
            out_tokens.append(token_string)

        if token_type not in IGNORED_TOKENS:
            last_significant_token = token_string

        prev_toktype = token_type
        last_lineno = end_line
        last_col = end_col

    cleaned = "".join(out_tokens)

    lines = cleaned.split("\n")
    result_lines = []
    blank_run = 0
    for ln in lines:
        if ln.strip() == "":
            blank_run += 1
            if blank_run <= 1:
                result_lines.append("")
        else:
            blank_run = 0
            result_lines.append(ln.rstrip())

    return "\n".join(result_lines).strip("\n") + "\n"


def main():
    from tokenize import TokenError
    from sys import stderr
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='path to input file', required=True)
    action = parser.add_mutually_exclusive_group()
    action.add_argument('-o', '--output', help='path to output file')
    action.add_argument('-O', '--overwrite', action='store_true', help='overwrite input file')
    parser.add_argument('-p', '--print', action='store_true', help='print output to stdout')
    args = parser.parse_args()

    if not args.print and not args.overwrite and args.output is None:
        print("Select output format with -p, -O or -o {filepath}")
        exit(1)

    input_path = args.input
    output_path = args.input if args.overwrite else args.output

    with open(input_path, "r", encoding="utf-8") as f:
        source = f.read()

    try:
        cleaned = remove_comments_and_docstrings(source)
    except TokenError as e:
        print(f"Failed to tokenize {input_path}: {e}", file=stderr)
        exit(1)

    if output_path is not None:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(cleaned)
        print(f"Wrote cleaned file to {output_path}")

    if args.print:
        print(cleaned)


if __name__ == "__main__":
    main()
