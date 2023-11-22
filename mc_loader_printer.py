import os

class MCLoaderPrinter:
    class fg:
        BLACK           = '\033[30m'
        RED             = '\033[31m'
        GREEN           = '\033[32m'
        YELLOW          = '\033[33m'
        BLUE            = '\033[34m'
        MAGENTA         = '\033[35m'
        CYAN            = '\033[36m'
        LIGHTGRAY       = '\033[37m'
        RESET           = '\033[39m'
        DARKGRAY        = '\033[90m'
        LIGHTRED        = '\033[91m'
        LIGHTGREEN      = '\033[92m'
        YELLOW          = '\033[93m'
        LIGHTBLUE       = '\033[94m'
        PINK            = '\033[95m'
        LIGHTCYAN       = '\033[96m'
    
    class bg:
        BLACK           = '\033[40m'
        RED             = '\033[41m'
        GREEN           = '\033[42m'
        ORANGE          = '\033[43m'
        BLUE            = '\033[44m'
        MAGENTA         = '\033[45m'
        CYAN            = '\033[46m'
        LIGHTGRAY       = '\033[47m'
        RESET           = '\033[49m'

    class style:
        RESET_ALL       = '\033[0m'
        BOLD            = '\033[1m'
        DISABLE         = '\033[2m'
        UNDERLINE       = '\033[4m'
        BLINK           = '\033[5m'
        REVERSE         = '\033[7m'
        HIDDEN          = '\033[8m'
        STRIKETHROUGH   = '\033[9m'
        NORMAL          = '\033[22m'

    def show_colors(self, text_to_show="Test"):
        """
        Prints all the available colors, background colors, and styles.

        Args:
            text (str): The text to be printed with all the available colors, background colors, and styles.
        """
        for fg in self.fg.__dict__:
            if fg[:2] != "__" and fg != "RESET":
                infos = f"FG: {fg} - "
                print(f"{infos}{self.fg.__dict__[fg]}"+ str(text_to_show) + f"{self.style.RESET_ALL}")
        for bg in self.bg.__dict__:
            if bg[:2] != "__" and bg != "RESET":
                infos = f"BG: {bg} - "
                print(f"{infos}{self.bg.__dict__[bg]}"+ str(text_to_show) + f"{self.style.RESET_ALL}")
        for style in self.style.__dict__:
            if style[:2] != "__" and style != "RESET_ALL":
                infos = f"STYLE: {style} - "
                print(f"{infos}{self.style.__dict__[style]}"+ str(text_to_show) + f"{self.style.RESET_ALL}")

    def clear_console(self):
        """
        Clears the console.
        """
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def calculate_color_length(self, text):
        """
        Calculates the length of the text with color codes.

        Args:
            text (str): The text to calculate the length of.

        Returns:
            int: The length of the text with color codes.
        """
        color_length = 0
        add = False
        for char in text:
            if char == "\033": # find the m in \033[m
                add = True
            if add:
                color_length += 1
            if char == "m":
                add = False
        
        return color_length

    def __init__(self,
                 case_bg="",
                 case_char="*",
                 case_color=fg.LIGHTBLUE,
                 case_style="",
                 case_empty_bg="",
                 case_empty_color=fg.YELLOW,
                 case_empty_style="",
                 case_loading_bg="",
                 case_loading_color=fg.LIGHTBLUE,
                 case_loading_style="",
                 is_case=True,
                 length=100,
                 loading_bar_bg="",
                 loading_bar_char="[]",
                 loading_bar_color=fg.LIGHTGRAY,
                 loading_bar_length=80,
                 loading_bar_style="",
                 loading_bg="",
                 loading_empty_bg="",
                 loading_empty_char="-",
                 loading_empty_color=fg.LIGHTRED,
                 loading_empty_style="",
                 loading_char="#",
                 loading_color=fg.LIGHTGREEN,
                 loading_style="",
                 subtitle="",
                 title="Program",
                 title_bg="",
                 title_color=fg.YELLOW,
                 title_space=False,
                 title_style=""
                ):
        """
        Initialize the MCLoaderPrinter object.

        Parameters:
        - case_bg (str): Background color for the case.
        - case_char (str): Character used for the case.
        - case_color (str): Color for the case.
        - case_style (str): Style for the case.
        - case_empty_bg (str): Background color for the empty case.
        - case_empty_color (str): Color for the empty case.
        - case_empty_style (str): Style for the empty case.
        - case_loading_bg (str): Background color for the loading case.
        - case_loading_color (str): Color for the loading case.
        - case_loading_style (str): Style for the loading case.
        - is_case (bool): Flag indicating whether to display the case.
        - length (int): Length of the loading bar.
        - loading_bar_bg (str): Background color for the loading bar.
        - loading_bar_char (str): Characters used for the loading bar.
        - loading_bar_color (str): Color for the loading bar.
        - loading_bar_length (int): Length of the loading bar.
        - loading_bar_style (str): Style for the loading bar.
        - loading_bg (str): Background color for the loading animation.
        - loading_empty_bg (str): Background color for the empty loading animation.
        - loading_empty_char (str): Character used for the empty loading animation.
        - loading_empty_color (str): Color for the empty loading animation.
        - loading_empty_style (str): Style for the empty loading animation.
        - loading_char (str): Character used for the loading animation.
        - loading_color (str): Color for the loading animation.
        - loading_style (str): Style for the loading animation.
        - subtitle (str): Subtitle for the loading bar.
        - title (str): Title for the loading bar.
        - title_bg (str): Background color for the title.
        - title_color (str): Color for the title.
        - title_space (bool): Flag indicating whether to add space between the title and the loading bar.
        - title_style (str): Style for the title.
        """
        self.length = length
        if length < 30:
            raise ValueError("Length cannot be less than 30.")

        self.case_char = case_char
        self.case_color = case_color
        self.case_style = case_style
        self.case_bg = case_bg
        self.is_case = is_case

        self.case_loading_color = case_loading_color
        self.case_loading_style = case_loading_style
        self.case_loading_bg = case_loading_bg

        self.case_empty_color = case_empty_color
        self.case_empty_style = case_empty_style
        self.case_empty_bg = case_empty_bg

        if loading_bar_length > length - 4:
            raise ValueError("Loading bar length cannot be greater than the length of the bar.")
        self.loading_bar_length = loading_bar_length

        self.loading_bar_color = loading_bar_color
        self.loading_bar_style = loading_bar_style
        self.loading_bar_bg = loading_bar_bg

        self.loading_color = loading_color
        self.loading_style = loading_style
        self.loading_bg = loading_bg

        self.loading_empty_color = loading_empty_color
        self.loading_empty_style = loading_empty_style
        self.loading_empty_bg = loading_empty_bg

        if len(loading_char) != 1:
            raise ValueError("Loading char must be of length 1.")
        self.loading_char = loading_char
        if len(loading_empty_char) != 1:
            raise ValueError("Empty char must be of length 1.")
        self.loading_empty_char = loading_empty_char
        if len(loading_bar_char) != 2:
            raise ValueError("Loading bar char must be of length 2.")
        self.opening_loading_bar_char = loading_bar_char[0]
        self.closing_loading_bar_char = loading_bar_char[1]

        self.title_space = title_space
        if len(title) - self.calculate_color_length(title) > length - 2:
            raise ValueError(f"Title is too long for the bar. Title length: {len(title)}, Bar length: {length}")
        self.title = title
        self.subtitle = subtitle
        self.title_color = title_color
        self.title_style = title_style
        self.title_bg = title_bg

        if len(subtitle) - self.calculate_color_length(subtitle) > length - 2:
            raise ValueError("Subtitle is too long for the bar.")

        self.subtitle = subtitle

    def set_new_subtitle(self, subtitle=""):
        """
        Sets a new subtitle for the bar.

        Args:
            subtitle (str): The new subtitle to set.

        Raises:
            ValueError: If the length of the subtitle is greater than the available space in the bar.

        """
        if len(subtitle) - self.calculate_color_length(subtitle) > self.length - 2:
            raise ValueError("Subtitle is too long for the bar.")
        
        self.subtitle = subtitle

    def color_text(self, fg="", text="", bg="", style=[]):
        """
        Formats the given text with the specified foreground color, background color, and style(s).

        Args:
            fg (str): The foreground color.
            text (str): The text to be formatted.
            bg (str, optional): The background color. Defaults to "".
            style (list, optional): The style. Defaults to [].

        Returns:
            str: The formatted text.
        """
        style = "".join(style)
        return f"{fg}{bg}{style}{text}{MCLoaderPrinter.style.RESET_ALL}"
    
    def get_all_styles(self, text):
        """
        Extracts the foreground color, background color, and style(s) from the given text.
        If the text contains a reset, it will reset the string to "".
        So if the text contains multiple resets or multiple colors, it will only return the last ones.

        Args:
            text (str): The text containing ANSI escape sequences for styling.

        Returns:
            tuple: A tuple containing the foreground color, background color, and style.
        """
        fg, bg, style = "", "", []
        # From the start, add the styles to the string (fg, bg, style), if we found a reset all we set the string to ""
        capture_str = ""
        for char in text:
            if capture_str != "" and char == "\033":
                capture_str = ""
            if char == "\033":
                capture_str = char
                continue
            if capture_str != "":
                capture_str += char
                if char == "m":
                    if capture_str == MCLoaderPrinter.style.RESET_ALL:
                        fg, bg, style = "", "", []
                        capture_str = ""
                    else:
                        if (capture_str[2] == "3" or capture_str[2] == "9") and capture_str[3] != "m":
                            fg = capture_str
                        elif capture_str[2] == "4" and capture_str[3] != "m":
                            bg = capture_str
                        else:
                            style.append(capture_str)
                        capture_str = ""
        return (fg, bg, style)

    def split_if_too_long(self, text):
        """
        Splits the given text into multiple lines if it exceeds the maximum length.
        It will split the text at the last space before the maximum length.
        If there is no space, it will split at the maximum length.
        It will also avoid splitting a color code.
        
        Args:
            text (str): The text to be split.

        Returns:
            list: A list of strings, each representing a line of the split text.
        """
        color_length = self.calculate_color_length(text)
        real_length = len(text) - color_length

        max_length = self.length - (0 if self.is_case else 2)
        if real_length < max_length:
            return [text]
        
        min_length = int(self.length * 0.1)
        (fg, bg, style) = ("", "", [])
        splited_text = []
        while True:
            if fg != "" or bg != "" or style != []:
                style = "".join(style)
                text = f"{fg}{bg}{style}{text}"
                style = []
            if len(text) < max_length:
                splited_text.append(text)
                break
            # Find the last space before the max_length
            last_space_index = text[:max_length].rfind(" ")
            offset = 1
            if last_space_index == -1:
                offset = 0
                last_space_index = max_length
                # if the last index fall on a color code, we need to remove it
                for i in range(1, 4):
                    if text[last_space_index - i] == "\033":
                        last_space_index -= i
                        break
                    
            # If the last space is too far away from the max_length, we need to split at the max_length
            if last_space_index < min_length:
                last_space_index = max_length
            
            text_to_add = text[:last_space_index]
            
            # Get the styles of the text to add
            (fg, bg, style) = self.get_all_styles(text_to_add)
            if fg != "" or bg != "" or style != []:
                text_to_add += MCLoaderPrinter.style.RESET_ALL
            splited_text.append(text_to_add)
            text = text[last_space_index + offset:]

        return splited_text
    
    def print_line(self, text="", full_case=False):
        """
        Prints a line of text with optional casing. If the text is too long, it will be split smartly into multiple lines.

        Args:
            text (str): The text to be printed.
            full_case (bool, optional): Whether to print the line with full casing. Defaults to False.
        """
        if full_case:
            print(self.color_text(self.case_color, self.case_char * self.length, self.case_bg, self.case_style))
        else:
            splited_text = self.split_if_too_long(text)
            for text in splited_text:
                text_color_length = self.calculate_color_length(text)
                if self.is_case:
                    colored_case = self.color_text(self.case_color, self.case_char, self.case_bg, self.case_style)
                    print(f"{colored_case}{text.center(self.length - 2 + text_color_length, ' ')}{colored_case}")
                else:
                    print(text.center(self.length + text_color_length, ' '))

    def print_lines(self, lines=[]):
        """
        Prints each line in the given list of lines.

        Args:
            lines (list): A list of strings representing the lines to be printed.
        """
        for line in lines:
            self.print_line(line)

    def print_loader(self, load_current=-1, load_end=-1, is_footer=False, space_before=False, space_after=False):
        """
        Prints a loader bar based on the current load and end load.

        Args:
            load_current (int): The current load value. Default is -1.
            load_end (int): The end load value. Default is -1.
            is_footer (bool): Indicates if the loader is a footer. Default is False.
            space_before (bool): Indicates if a blank line should be printed before the loader. Default is False.
            space_after (bool): Indicates if a blank line should be printed after the loader. Default is False.

        Raises:
            ValueError: If the current load is greater than the end load.

        Returns:
            None
        """
        if load_current < 0 or load_end < 0:
            return
        if load_current > load_end:
            raise ValueError("Current load cannot be greater than the end load.")
        if space_before:
            self.print_line("")
        if is_footer:
            bar_length = self.length - 2
        else:
            bar_length = self.loading_bar_length

        filled_length = int(bar_length * load_current // load_end)
        empty_length = bar_length - filled_length
        
        full_bar=""
        if is_footer:
            filled_bar = self.color_text(self.case_loading_color, self.loading_char * filled_length, self.case_loading_bg, self.case_loading_style)
            empty_bar = self.color_text(self.case_empty_color, self.loading_empty_char * empty_length, self.case_empty_bg, self.case_empty_style)
            full_bar = f"{filled_bar}{empty_bar}"
        else:
            filled_bar = self.color_text(self.loading_color, self.loading_char * filled_length, self.loading_bg, self.loading_style)
            empty_bar = self.color_text(self.loading_empty_color, self.loading_empty_char * empty_length, self.loading_empty_bg, self.loading_empty_style)
            open_bar = self.color_text(self.loading_bar_color, self.opening_loading_bar_char, self.loading_bar_bg, self.loading_bar_style)
            close_bar = self.color_text(self.loading_bar_color, self.closing_loading_bar_char, self.loading_bar_bg, self.loading_bar_style)
            full_bar = f"{open_bar}{filled_bar}{empty_bar}{close_bar}"
        self.print_line(full_bar)

        if space_after:
            self.print_line("")

    def print_title(self, space_after=False):
        """
        Prints the title and subtitle with proper formatting.

        This method prints the title and subtitle using the specified formatting options. It first prints an empty line with full case formatting, then checks if there should be a space before the title. If so, it prints an empty line. Next, it prints the title using the specified color, background color, and style. If a subtitle is provided, it is printed as well. After that, if there should be a space after the title, it prints an empty line. Finally, it prints an empty line with full case formatting and an additional empty line.
        """
        self.print_line("", full_case=True)
        if self.title_space:
            self.print_line("")
        if self.title != "":
            self.print_line(self.color_text(self.title_color, self.title, self.title_bg, self.title_style))
        if self.subtitle != "":
            self.print_line(self.subtitle)
        if self.title_space:
            self.print_line("")
        self.print_line("", full_case=True)
        if space_after:
            self.print_line("")

    def print_footer(self, load_current=-1, load_end=-1, space_before=False):
        """
        Prints the footer section of the loader printer.

        Args:
            load_current (int): The current load value. Defaults to -1.
            load_end (int): The end load value. Defaults to -1.
            space_before (bool): Indicates if a blank line should be printed before the footer. Defaults to False.

        Raises:
            ValueError: If the current load is greater than the end load.
        """
        if space_before:
            self.print_line("")
        self.print_line("", full_case=True)
        if load_current < 0 or load_end < 0:
            print("\n" * 5)
            return
        if load_current > load_end:
            raise ValueError("Current load cannot be greater than the end load.")
        self.print_loader(load_current, load_end, is_footer=True)
        self.print_line("", full_case=True)
        print("\n" * 5)

    def print_format(self, format={}, clear=True):
        """
        Prints the formatted output based on the given format dictionary.

        Args:
            format (dict): The format dictionary containing the structure of the output.
            clear (bool): Whether to clear the console before printing the output.

        Raises:
            ValueError: If the format dictionary is not valid.

        Returns:
            None
        """
        if clear:
            print("clearing console...")
            self.clear_console()
        
        if "subtitle" in format:
            if not isinstance(format["subtitle"], str):
                raise ValueError("Subtitle must be a string.")
            self.set_new_subtitle(format["subtitle"])
        
        title_space = format["title_space"] if "title_space" in format else False
        self.print_title(space_after=title_space)

        if "body" in format:
            if not isinstance(format["body"], list):
                raise ValueError("Body must be a list.")
            for line in format["body"]:
                if "text" in line:
                    self.print_line(line["text"])
                elif "loader" in line:
                    space_before = line["loader"]["space_before"] if "space_before" in line["loader"] else False
                    space_after = line["loader"]["space_after"] if "space_after" in line["loader"] else False
                    self.print_loader(
                        load_current=line["loader"]["load_current"],
                        load_end=line["loader"]["load_end"],
                        space_before=space_before,
                        space_after=space_after
                    )
                else:
                    self.print_line("")

        if "footer" in format:
            if not "load_current" in format["footer"] or not "load_end" in format["footer"]:
                raise ValueError("Missing mandatory fields in footer.")
            space_before = format["footer_space"] if "footer_space" in format else False
            self.print_footer(
                load_current=format["footer"]["load_current"],
                load_end=format["footer"]["load_end"],
                space_before=space_before
            )
        elif self.is_case and "body" in format and len(format["body"]) > 0:
            space_before = format["footer_space"] if "footer_space" in format else False
            self.print_footer(space_before=space_before)
        else:
            print("\n" * 5)
