def delete_empty_lines(output):
    output = output.strip().replace("\r\n", "\n")
    lines = []
    for line in output.split("\n"):
        if line.strip():
            lines.append(line.rstrip())
    return "\n".join(lines)

