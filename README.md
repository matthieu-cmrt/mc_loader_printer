# MCPrettyLoader

# Introduction

MCPrettyLoader is an accessible tool thats allows users to implement easily visual for their loaders. The features are easy-to-use and allow users to create pretty loader with a minimum of code.

The concept is to send a unique object to the tool and it will create (respecting your settings) a loader with all the informations you want in it and display it in your console.

With MCPrettyLoader, the users can also easily color text which is a feature used for the loader itself.

# Installation

For the moment, I couldn't create the librairy. You will need 'python 3.x'.
For installation, you need to download or clone the repository, then you should take the 'mc_pretty_loader.py' file into your project architecture. I suggest you move the file into a 'utils' directory

In your project, you will need to import the class :
```py
from utils.mc_pretty_loader import MCPrettyLoader
```

# Usage

## Foreground, Background and Style
The class also permit access to 3 class (fg, bg and style).
For foreground class (MCPrettyLoader.fg) as for background class(MCPrettyLoader.bg), you can use thoses colors :
```py
    - BLACK
    - RED
    - GREEN
    - ORANGE
    - BLUE
    - MAGENTA
    - CYAN
    - LIGHTGRAY
    - DARKGRAY
    - LIGHTRED
    - LIGHTGREEN
    - YELLOW
    - LIGHTBLUE
    - PINK
    - LIGHTCYAN
    - WHITE
```

As for style (MCPrettyLoader.style), you have access to :
```py
    - RESET_ALL
    - BOLD
    - DISABLE
    - UNDERLINE
    - BLINK
    - REVERSE
    - HIDDEN
    - STRIKETHROUGH
```

To see how each one of them can be used, you can use the fonction **MCPrettyLoader.display_colors(text_to_show)** which will display the text (by default "Test") in each color/style.

## Initialization
The object MCPrettyLoader can be initialized with many arguments :

### Body parameter
```py
- body_padding (int, optional): The padding around the body content. Defaults to 0.
```

### Casing parameters
```py
- case_bg (str, optional): The background color of the case. Defaults to "".
- case_char (str, optional): The character used for the case. Defaults to "*".
- case_color (str, optional): The color of the case. Defaults to fg.LIGHTBLUE.
- case_style (list, optional): The style of the case. Defaults to [].
- case_empty_bg (str, optional): The background color of the empty case. Defaults to "".
- case_empty_color (str, optional): The color of the empty case. Defaults to fg.YELLOW.
- case_empty_style (list, optional): The style of the empty case. Defaults to [].
- case_loading_bg (str, optional): The background color of the loading case. Defaults to "".
- case_loading_color (str, optional): The color of the loading case. Defaults to fg.LIGHTBLUE.
- case_loading_style (list, optional): The style of the loading case. Defaults to [].
```

### Footer parameters
```py
- footer_loading_bg (str, optional): The background color of the footer loading bar. Defaults to "".
- footer_loading_char (str, optional): The character used for the footer loading bar. Defaults to "#".
- footer_loading_color (str, optional): The color of the footer loading bar. Defaults to fg.BLUE.
- footer_loading_style (list, optional): The style of the footer loading bar. Defaults to [].
- footer_loading_empty_bg (str, optional): The background color of the empty footer loading bar. Defaults to "".
- footer_loading_empty_char (str, optional): The character used for the empty footer loading bar. Defaults to "-".
- footer_loading_empty_color (str, optional): The color of the empty footer loading bar. Defaults to fg.YELLOW.
- footer_loading_empty_style (list, optional): The style of the empty footer loading bar. Defaults to [].
- footer_loading_reverse (bool, optional): Whether to reverse the footer loading bar. Defaults to False.
- footer_loading_thickness (int, optional): The thickness of the footer loading bar. Defaults to 1.
```

### Loader is cased ?
```py
- is_case (bool, optional): Whether to display the case. Defaults to True.
```

### Left side parameters
```py
- left_side_bar_loader_bg (str, optional): The background color of the left side bar loader. Defaults to "".
- left_side_bar_loader_char (str, optional): The character used for the left side bar loader. Defaults to "V".
- left_side_bar_loader_color (str, optional): The color of the left side bar loader. Defaults to fg.GREEN.
- left_side_bar_loader_style (list, optional): The style of the left side bar loader. Defaults to [].
- left_side_bar_loader_empty_bg (str, optional): The background color of the empty left side bar loader. Defaults to "".
- left_side_bar_loader_empty_char (str, optional): The character used for the empty left side bar loader. Defaults to "v".
- left_side_bar_loader_empty_color (str, optional): The color of the empty left side bar loader. Defaults to fg.RED.
- left_side_bar_loader_empty_style (list, optional): The style of the empty left side bar loader. Defaults to [].
- left_side_bar_loader_is_case (bool, optional): Whether to display the left side bar loader as a case. Defaults to True.
- left_side_bar_loader_on_title (bool, optional): Whether to display the left side bar loader on the title. Defaults to False.
- left_side_bar_loader_on_footer (bool, optional): Whether to display the left side bar loader on the footer. Defaults to False.
- left_side_bar_loader_reverse (bool, optional): Whether to reverse the left side bar loader. Defaults to False.
- left_side_bar_loader_thickness (int, optional): The thickness of the left side bar loader. Defaults to 1.
```

### Size parameter
```py
- length (int, optional): The total length of the progress bar. Defaults to 100.
```

### Loading Bar parameters
```py
- loading_bar_bg (str, optional): The background color of the loading bar. Defaults to "".
- loading_bar_char (str, optional): The characters used for the loading bar. Defaults to "[]".
- loading_bar_color (str, optional): The color of the loading bar. Defaults to fg.LIGHTGRAY.
- loading_bar_length (int, optional): The length of the loading bar. Defaults to 0.
- loading_bar_style (list, optional): The style of the loading bar. Defaults to [].
- loading_bg (str, optional): The background color of the loading animation. Defaults to "".
- loading_empty_bg (str, optional): The background color of the empty loading animation. Defaults to "".
- loading_empty_char (str, optional): The character used for the empty loading animation. Defaults to "-".
- loading_empty_color (str, optional): The color of the empty loading animation. Defaults to fg.LIGHTRED.
- loading_empty_style (list, optional): The style of the empty loading animation. Defaults to [].
- loading_char (str, optional): The character used for the loading animation. Defaults to "#".
- loading_color (str, optional): The color of the loading animation. Defaults to fg.LIGHTGREEN.
- loading_reverse (bool, optional): Whether to reverse the loading animation. Defaults to False.
- loading_style (list, optional): The style of the loading animation. Defaults to [].
- loading_thickness (int, optional): The thickness of the loading animation. Defaults to 1.
```

### External parameter
```py
- margin (int, optional): The margin around the progress bar. Defaults to 0.
```

### Right Sider parameters
```py
- right_side_bar_loader_bg (str, optional): The background color of the right side bar loader. Defaults to "".
- right_side_bar_loader_char (str, optional): The character used for the right side bar loader. Defaults to "V".
- right_side_bar_loader_color (str, optional): The color of the right side bar loader. Defaults to fg.GREEN.
- right_side_bar_loader_style (list, optional): The style of the right side bar loader. Defaults to [].
- right_side_bar_loader_empty_bg (str, optional): The background color of the empty right side bar loader. Defaults to "".
- right_side_bar_loader_empty_char (str, optional): The character used for the empty right side bar loader. Defaults to "v".
- right_side_bar_loader_empty_color (str, optional): The color of the empty right side bar loader. Defaults to fg.RED.
- right_side_bar_loader_empty_style (list, optional): The style of the empty right side bar loader. Defaults to [].
- right_side_bar_loader_is_case (bool, optional): Whether to display the right side bar loader as a case. Defaults to True.
- right_side_bar_loader_on_title (bool, optional): Whether to display the right side bar loader on the title. Defaults to False.
- right_side_bar_loader_on_footer (bool, optional): Whether to display the right side bar loader on the footer. Defaults to False.
- right_side_bar_loader_reverse (bool, optional): Whether to reverse the right side bar loader. Defaults to False.
- right_side_bar_loader_thickness (int, optional): The thickness of the right side bar loader. Defaults to 1.
```

### Title parameters
```py
- subtitle (str, optional): The subtitle of the progress bar. Defaults to "".
- title (str, optional): The title of the progress bar. Defaults to "Program".
- title_bg (str, optional): The background color of the title. Defaults to "".
- title_color (str, optional): The color of the title. Defaults to fg.ORANGE.
- title_space (bool, optional): Whether to add a space between the title and the progress bar. Defaults to False.
- title_style (list, optional): The style of the title. Defaults to [style.BOLD, style.UNDERLINE].
```

## Coloring text
To color easily a text, the class has a fonction made to simplify this process:
```py
    color_text(self, fg=self.fg.RED, text="This is a test", bg=self.bg=YELLOW, style=[self.style.UNDERLINE])
```

## Object creation

# Examples
