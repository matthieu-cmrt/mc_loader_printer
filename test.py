from mc_loader_printer import MCLoaderPrinter
import os

# clear()
if os.name == "nt":
    os.system("cls")
else:
    os.system("clear")

def setup(is_case=False, has_subtitle=False, size=100, loading_bar_length=80, title_space=False):
    LP = MCLoaderPrinter(
        title="Test", title_space=title_space,
        case_char="#", length=size,
        loading_bar_length=loading_bar_length,
        is_case=is_case
        )

    if not has_subtitle:
        return LP
    
    subtitle = LP.color_text(
        fg=LP.fg.GREEN,
        text="This is a"
    )
    subtitle += LP.color_text(
        fg=LP.fg.RED,
        text=" test"
    ) + LP.color_text(
        fg=LP.fg.GREEN,
        text="."
    )
    LP.set_new_subtitle(subtitle)
    return LP

def get_colored_text(LP):
   return LP.color_text(
        fg=LP.fg.RED,
        text="This is a test."
    )

def get_difficult_text(LP):
    return "Hello world, my name is " + LP.color_text(
        fg=LP.fg.RED,
        text="JOHN DOE DE SAINTE-CROIX DE NEUVILLE",
        bg=LP.bg.YELLOW,
        style=LP.style.DIM
    ) + " and I am " + LP.color_text(
        fg=LP.fg.BLUE,
        text="20 years old"
    ) + " and I live in " + LP.color_text(
        fg=LP.fg.GREEN,
        text="New York City"
    ) + "!"

def get_huge_format_print(LP):
    return {
        "title_space": True, 
        "subtitle": get_colored_text(LP),
        "footer": { 
            "load_current": 7, 
            "load_end": 39, 
        },
        "footer_space": True, 
        "body": [
            {},
            {
                "text": get_difficult_text(LP),
            },
            {
                "loader": { 
                    "load_current": 328, 
                    "load_end": 838, 
                    "space_before": True, 
                    "space_after": True, 
                }
            },
            {}
        ]
    }

def get_huge_no_footer_format_print(LP):
    return {
        "title_space": True, 
        "subtitle": get_colored_text(LP),
        "footer_space": True, 
        "body": [
            {},
            {
                "text": get_difficult_text(LP),
            },
            {
                "loader": { 
                    "load_current": 328, 
                    "load_end": 838, 
                    "space_before": True, 
                    "space_after": True, 
                }
            },
            {}
        ]
    }

def get_easy_format_print(LP):
    return {
        "title_space": True,
        "body": [
            {
                "text": get_colored_text(LP)
            }
        ]
    }

def no_footer():
    return {
        "body": [
            {}
        ]
    }

def test_normal():
    LP = setup()
    LP.print_title()
    LP.print_lines(
        [
            "Hello World!",
        ]
    )
    LP.print_footer()

def test_casing():
    is_case = True
    title_space = True
    LP = setup(is_case=is_case, title_space=title_space)
    LP.print_title(space_after=True)
    LP.print_lines(
        [
            "Hello World!",
        ]
    )
    LP.print_footer(space_before=True)

def test_subtitle():
    is_case = True
    title_space = True
    has_subtitle = True
    LP = setup(is_case=is_case, title_space=title_space, has_subtitle=has_subtitle)
    LP.print_title(space_after=True)
    LP.print_lines(
        [
            "Hello World!",
        ]
    )
    LP.print_footer(space_before=True)

def test_huge_format():
    is_case = True
    title_space = True
    LP = setup(
        is_case=is_case, 
        title_space=title_space
    )
    format = get_huge_format_print(LP)
    LP.print_format(format)

def test_huge_format_50_length():
    is_case = True
    title_space = True
    LP = setup(
        is_case=is_case, 
        title_space=title_space,
        size=50,
        loading_bar_length=30
    )
    format = get_huge_format_print(LP)
    LP.print_format(format)

def test_easy_format_no_case():
    LP = setup()
    format = get_easy_format_print(LP)
    LP.print_format(format)

def test_easy_format():
    is_case = True
    LP = setup(is_case=is_case)
    format = get_easy_format_print(LP)
    LP.print_format(format)

def test_no_footer():
    is_case = True
    title_space = True
    LP = setup(is_case=is_case, title_space=title_space)
    format = no_footer()
    LP.print_format(format)

def test_huge_no_footer():
    is_case = True
    title_space = True
    LP = setup(is_case=is_case, title_space=title_space)
    format = get_huge_no_footer_format_print(LP)
    LP.print_format(format)

def show_colors():
    LP = setup()
    LP.show_colors()

if __name__ == "__main__":
    # test_normal()
    # test_casing()
    # test_subtitle()
    # test_huge_format()
    # test_huge_format_50_length()
    # test_easy_format_no_case()
    # test_easy_format()
    # test_no_footer()
    # test_huge_no_footer()
    show_colors()