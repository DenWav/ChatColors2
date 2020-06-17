print("public final class ChatColors2 {")
for r in range(256):
    print(f"    public static final class R{r:03} {{")
    for g in range(256):
        print(f"        public static enum G{g:03} {{")
        for b in range(256):
            print(f"            B{b:03}({r}, {g}, {b}),")
        print("            ;")
        print("            public final int r; public final int g; public final int b;")
        print(f"            G{g:03}(final int r, final int g, final int b) {{")
        print("                this.r = r; this.g = g; this.b = b;")
        print("            }")
        print("        }")
    print("    }")
print("}")

