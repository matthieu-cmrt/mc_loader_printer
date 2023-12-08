import os

class MCPrettyLoader:
    class fg:
        BLACK           = '\033[30m'
        RED             = '\033[31m'
        GREEN           = '\033[32m'
        ORANGE          = '\033[33m'
        BLUE            = '\033[34m'
        MAGENTA         = '\033[35m'
        CYAN            = '\033[36m'
        LIGHTGRAY       = '\033[37m'
        DARKGRAY        = '\033[90m'
        LIGHTRED        = '\033[91m'
        LIGHTGREEN      = '\033[92m'
        YELLOW          = '\033[93m'
        LIGHTBLUE       = '\033[94m'
        PINK            = '\033[95m'
        LIGHTCYAN       = '\033[96m'
        WHITE           = '\033[97m'

    class bg:
        BLACK           = '\033[40m'
        RED             = '\033[41m'
        GREEN           = '\033[42m'
        ORANGE          = '\033[43m'
        BLUE            = '\033[44m'
        MAGENTA         = '\033[45m'
        CYAN            = '\033[46m'
        LIGHTGRAY       = '\033[47m'
        DARKGRAY        = '\033[100m'
        LIGHTRED        = '\033[101m'
        LIGHTGREEN      = '\033[102m'
        YELLOW          = '\033[103m'
        LIGHTBLUE       = '\033[104m'
        PINK            = '\033[105m'
        LIGHTCYAN       = '\033[106m'
        WHITE           = '\033[107m'

    class style:
        RESET_ALL       = '\033[0m'
        BOLD            = '\033[1m'
        DISABLE         = '\033[2m'
        UNDERLINE       = '\033[4m'
        BLINK           = '\033[5m'
        REVERSE         = '\033[7m'
        HIDDEN          = '\033[8m'
        STRIKETHROUGH   = '\033[9m'

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

    """
        left_side_bar_loader = {
            color
            load_char
            load_color
            empty_char
            empty_color
            thickness
        }
        same for right_side_bar_loader

        add thickness to the bar loader and also to the footer loader
        raise error if thickness is too big (max 5) or too small (min 1)
        raise error if the bar loader is too big (max depends on the length of the bar) or too small (min 1)
    """
    def __init__(
                self,
                body_padding=0,
                case_bg="",
                case_char="*",
                case_color=fg.LIGHTBLUE,
                case_style=[],
                case_empty_bg="",
                case_empty_color=fg.YELLOW,
                case_empty_style=[],
                case_loading_bg="",
                case_loading_color=fg.LIGHTBLUE,
                case_loading_style=[],
                footer_loading_bg="",
                footer_loading_char="#",
                footer_loading_color=fg.BLUE,
                footer_loading_style=[],
                footer_loading_empty_bg="",
                footer_loading_empty_char="-",
                footer_loading_empty_color=fg.YELLOW,
                footer_loading_empty_style=[],
                footer_loading_reverse=False,
                footer_loading_thickness=1,
                is_case=True,
                left_side_bar_loader_bg="",
                left_side_bar_loader_char="V",
                left_side_bar_loader_color=fg.GREEN,
                left_side_bar_loader_style=[],
                left_side_bar_loader_empty_bg="",
                left_side_bar_loader_empty_char="v",
                left_side_bar_loader_empty_color=fg.RED,
                left_side_bar_loader_empty_style=[],    
                left_side_bar_loader_is_case=True,
                left_side_bar_loader_on_title=False,
                left_side_bar_loader_on_footer=False,
                left_side_bar_loader_reverse=False,
                left_side_bar_loader_thickness=1,
                length=100,
                loading_bar_bg="",
                loading_bar_char="[]",
                loading_bar_color=fg.LIGHTGRAY,
                loading_bar_length=0,
                loading_bar_style=[],
                loading_bg="",
                loading_empty_bg="",
                loading_empty_char="-",
                loading_empty_color=fg.LIGHTRED,
                loading_empty_style=[],
                loading_char="#",
                loading_color=fg.LIGHTGREEN,
                loading_reverse=False,
                loading_style=[],
                loading_thickness=1,
                margin=0,
                right_side_bar_loader_bg="",
                right_side_bar_loader_char="V",
                right_side_bar_loader_color=fg.GREEN,
                right_side_bar_loader_style=[],
                right_side_bar_loader_empty_bg="",
                right_side_bar_loader_empty_char="v",
                right_side_bar_loader_empty_color=fg.RED,
                right_side_bar_loader_empty_style=[],
                right_side_bar_loader_is_case=True,
                right_side_bar_loader_on_title=False,
                right_side_bar_loader_on_footer=False,
                right_side_bar_loader_reverse=False,
                right_side_bar_loader_thickness=1,
                subtitle="",
                title="Program",
                title_bg="",
                title_color=fg.ORANGE,
                title_space=False,
                title_style=[style.BOLD, style.UNDERLINE]
                ):
        """
        Initialize the mc_pretty_loader object with the specified parameters.

        Args:
            body_padding (int, optional): The padding around the body content. Defaults to 0.
            case_bg (str, optional): The background color of the case. Defaults to "".
            case_char (str, optional): The character used for the case. Defaults to "*".
            case_color (str, optional): The color of the case. Defaults to fg.LIGHTBLUE.
            case_style (list, optional): The style of the case. Defaults to [].
            case_empty_bg (str, optional): The background color of the empty case. Defaults to "".
            case_empty_color (str, optional): The color of the empty case. Defaults to fg.YELLOW.
            case_empty_style (list, optional): The style of the empty case. Defaults to [].
            case_loading_bg (str, optional): The background color of the loading case. Defaults to "".
            case_loading_color (str, optional): The color of the loading case. Defaults to fg.LIGHTBLUE.
            case_loading_style (list, optional): The style of the loading case. Defaults to [].
            footer_loading_bg (str, optional): The background color of the footer loading bar. Defaults to "".
            footer_loading_char (str, optional): The character used for the footer loading bar. Defaults to "#".
            footer_loading_color (str, optional): The color of the footer loading bar. Defaults to fg.BLUE.
            footer_loading_style (list, optional): The style of the footer loading bar. Defaults to [].
            footer_loading_empty_bg (str, optional): The background color of the empty footer loading bar. Defaults to "".
            footer_loading_empty_char (str, optional): The character used for the empty footer loading bar. Defaults to "-".
            footer_loading_empty_color (str, optional): The color of the empty footer loading bar. Defaults to fg.YELLOW.
            footer_loading_empty_style (list, optional): The style of the empty footer loading bar. Defaults to [].
            footer_loading_reverse (bool, optional): Whether to reverse the footer loading bar. Defaults to False.
            footer_loading_thickness (int, optional): The thickness of the footer loading bar. Defaults to 1.
            is_case (bool, optional): Whether to display the case. Defaults to True.
            left_side_bar_loader_bg (str, optional): The background color of the left side bar loader. Defaults to "".
            left_side_bar_loader_char (str, optional): The character used for the left side bar loader. Defaults to "V".
            left_side_bar_loader_color (str, optional): The color of the left side bar loader. Defaults to fg.GREEN.
            left_side_bar_loader_style (list, optional): The style of the left side bar loader. Defaults to [].
            left_side_bar_loader_empty_bg (str, optional): The background color of the empty left side bar loader. Defaults to "".
            left_side_bar_loader_empty_char (str, optional): The character used for the empty left side bar loader. Defaults to "v".
            left_side_bar_loader_empty_color (str, optional): The color of the empty left side bar loader. Defaults to fg.RED.
            left_side_bar_loader_empty_style (list, optional): The style of the empty left side bar loader. Defaults to [].
            left_side_bar_loader_is_case (bool, optional): Whether to display the left side bar loader as a case. Defaults to True.
            left_side_bar_loader_on_title (bool, optional): Whether to display the left side bar loader on the title. Defaults to False.
            left_side_bar_loader_on_footer (bool, optional): Whether to display the left side bar loader on the footer. Defaults to False.
            left_side_bar_loader_reverse (bool, optional): Whether to reverse the left side bar loader. Defaults to False.
            left_side_bar_loader_thickness (int, optional): The thickness of the left side bar loader. Defaults to 1.
            length (int, optional): The total length of the progress bar. Defaults to 100.
            loading_bar_bg (str, optional): The background color of the loading bar. Defaults to "".
            loading_bar_char (str, optional): The characters used for the loading bar. Defaults to "[]".
            loading_bar_color (str, optional): The color of the loading bar. Defaults to fg.LIGHTGRAY.
            loading_bar_length (int, optional): The length of the loading bar. Defaults to 0.
            loading_bar_style (list, optional): The style of the loading bar. Defaults to [].
            loading_bg (str, optional): The background color of the loading animation. Defaults to "".
            loading_empty_bg (str, optional): The background color of the empty loading animation. Defaults to "".
            loading_empty_char (str, optional): The character used for the empty loading animation. Defaults to "-".
            loading_empty_color (str, optional): The color of the empty loading animation. Defaults to fg.LIGHTRED.
            loading_empty_style (list, optional): The style of the empty loading animation. Defaults to [].
            loading_char (str, optional): The character used for the loading animation. Defaults to "#".
            loading_color (str, optional): The color of the loading animation. Defaults to fg.LIGHTGREEN.
            loading_reverse (bool, optional): Whether to reverse the loading animation. Defaults to False.
            loading_style (list, optional): The style of the loading animation. Defaults to [].
            loading_thickness (int, optional): The thickness of the loading animation. Defaults to 1.
            margin (int, optional): The margin around the progress bar. Defaults to 0.
            right_side_bar_loader_bg (str, optional): The background color of the right side bar loader. Defaults to "".
            right_side_bar_loader_char (str, optional): The character used for the right side bar loader. Defaults to "V".
            right_side_bar_loader_color (str, optional): The color of the right side bar loader. Defaults to fg.GREEN.
            right_side_bar_loader_style (list, optional): The style of the right side bar loader. Defaults to [].
            right_side_bar_loader_empty_bg (str, optional): The background color of the empty right side bar loader. Defaults to "".
            right_side_bar_loader_empty_char (str, optional): The character used for the empty right side bar loader. Defaults to "v".
            right_side_bar_loader_empty_color (str, optional): The color of the empty right side bar loader. Defaults to fg.RED.
            right_side_bar_loader_empty_style (list, optional): The style of the empty right side bar loader. Defaults to [].
            right_side_bar_loader_is_case (bool, optional): Whether to display the right side bar loader as a case. Defaults to True.
            right_side_bar_loader_on_title (bool, optional): Whether to display the right side bar loader on the title. Defaults to False.
            right_side_bar_loader_on_footer (bool, optional): Whether to display the right side bar loader on the footer. Defaults to False.
            right_side_bar_loader_reverse (bool, optional): Whether to reverse the right side bar loader. Defaults to False.
            right_side_bar_loader_thickness (int, optional): The thickness of the right side bar loader. Defaults to 1.
            subtitle (str, optional): The subtitle of the progress bar. Defaults to "".
            title (str, optional): The title of the progress bar. Defaults to "Program".
            title_bg (str, optional): The background color of the title. Defaults to "".
            title_color (str, optional): The color of the title. Defaults to fg.ORANGE.
            title_space (bool, optional): Whether to add a space between the title and the progress bar. Defaults to False.
            title_style (list, optional): The style of the title. Defaults to [style.BOLD, style.UNDERLINE].
        """
        # ========= Error handling =========

        def verifyBtw(value, min, max, name):
            if value < min or value > max:
                raise ValueError(f"{name} must be between {min} and {max} (included).")
            return value

        def verifyThickness(thickness):
            if thickness < 1 or thickness > 10:
                raise ValueError("Thickness must be between 1 and 10.")
            return thickness
    
        def verifyStr(string, supposed_len, name):
            if len(string) != supposed_len:
                raise ValueError(f"'{name}' must be of length {supposed_len}.")
            return string

        # ========= Length =========

        if length < 30:
            raise ValueError("Length cannot be less than 30.")
        self.length = length

        # ========= Margin =========

        self.margin = verifyBtw(margin, 0, 5, "Margin")

        # ========= Body =========
        
        self.body_padding = verifyBtw(body_padding, 0, 5, "Body padding")

        # ========= Case =========

        self.case_char = verifyStr(case_char, 1, "case_char")
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

        # ========= Footer loader =========

        self.footer_loading_color = footer_loading_color
        self.footer_loading_style = footer_loading_style
        self.footer_loading_bg = footer_loading_bg

        self.footer_loading_empty_color = footer_loading_empty_color
        self.footer_loading_empty_style = footer_loading_empty_style
        self.footer_loading_empty_bg = footer_loading_empty_bg

        self.footer_loading_char = verifyStr(footer_loading_char, 1, "footer_loading_char")
        self.footer_loading_empty_char = verifyStr(footer_loading_empty_char, 1, "footer_loading_empty_char")

        self.footer_loading_thickness = verifyThickness(footer_loading_thickness)

        self.footer_loading_reverse = footer_loading_reverse

        # ========= Left side bar loader =========

        self.left_side_bar_loader_is_case = left_side_bar_loader_is_case

        self.left_side_bar_loader_color = left_side_bar_loader_color
        self.left_side_bar_loader_style = left_side_bar_loader_style
        self.left_side_bar_loader_bg = left_side_bar_loader_bg

        self.left_side_bar_loader_empty_color = left_side_bar_loader_empty_color
        self.left_side_bar_loader_empty_style = left_side_bar_loader_empty_style
        self.left_side_bar_loader_empty_bg = left_side_bar_loader_empty_bg

        self.left_side_bar_loader_char = verifyStr(left_side_bar_loader_char, 1, "left_side_bar_loader_char")
        self.left_side_bar_loader_empty_char = verifyStr(left_side_bar_loader_empty_char, 1, "left_side_bar_loader_empty_char")

        self.left_side_bar_loader_thickness = verifyThickness(left_side_bar_loader_thickness)

        self.left_side_bar_loader_on_title = left_side_bar_loader_on_title
        self.left_side_bar_loader_on_footer = left_side_bar_loader_on_footer
        self.left_side_bar_loader_reverse = left_side_bar_loader_reverse

        # ========= Right side bar loader =========

        self.right_side_bar_loader_is_case = right_side_bar_loader_is_case

        self.right_side_bar_loader_color = right_side_bar_loader_color
        self.right_side_bar_loader_style = right_side_bar_loader_style
        self.right_side_bar_loader_bg = right_side_bar_loader_bg

        self.right_side_bar_loader_empty_color = right_side_bar_loader_empty_color
        self.right_side_bar_loader_empty_style = right_side_bar_loader_empty_style
        self.right_side_bar_loader_empty_bg = right_side_bar_loader_empty_bg

        self.right_side_bar_loader_char = verifyStr(right_side_bar_loader_char, 1, "right_side_bar_loader_char")
        self.right_side_bar_loader_empty_char = verifyStr(right_side_bar_loader_empty_char, 1, "right_side_bar_loader_empty_char")

        self.right_side_bar_loader_thickness = verifyThickness(right_side_bar_loader_thickness)

        self.right_side_bar_loader_on_title = right_side_bar_loader_on_title
        self.right_side_bar_loader_on_footer = right_side_bar_loader_on_footer
        self.right_side_bar_loader_reverse = right_side_bar_loader_reverse

        # ========= Loading bar =========
        max_length = self.length - (2 if self.is_case else 0) - (body_padding * 2)
        if loading_bar_length < 10 or loading_bar_length > max_length:
            self.loading_bar_length = max_length - 2
        else:
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

        self.loading_char = verifyStr(loading_char, 1, "loading_char")
        self.loading_empty_char = verifyStr(loading_empty_char, 1, "loading_empty_char")

        loading_bar_char = verifyStr(loading_bar_char, 2, "loading_bar_char")
        self.opening_loading_bar_char = loading_bar_char[0]
        self.closing_loading_bar_char = loading_bar_char[1]

        self.loading_thickness = verifyThickness(loading_thickness)

        self.loading_reverse = loading_reverse

        # ========= Title =========

        self.title_space = title_space
        self.title = title
        self.title_color = title_color
        self.title_style = title_style
        self.title_bg = title_bg

        self.subtitle = subtitle

        # ========= Printing_state =========
        self.is_already_printing = False
        # ========= END =========

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

    def display_colors(self, text_to_show="Test"):
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
        return f"{fg}{bg}{style}{text}{self.style.RESET_ALL}"
    
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
                    if capture_str == self.style.RESET_ALL:
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
        padding = self.body_padding * 2
        max_length = self.length - (2 if self.is_case else 0) - padding
        if real_length <= max_length:
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
                text_to_add += self.style.RESET_ALL
            splited_text.append(text_to_add)
            text = text[last_space_index + offset:]

        return splited_text
    
    def format_title(self, obj={}):
        content = []
        if self.title_space:
            content.append({})
        colored_title = self.color_text(
            self.title_color,
            self.title,
            self.title_bg,
            self.title_style
        )
        splited_title = self.split_if_too_long(colored_title)
        for st in splited_title:
            content.append({
                "text": st,
            })
        if 'subtitle_text' in obj:
            self.set_new_subtitle(obj['subtitle_text'])
        if self.subtitle != "":
            splited_subtitle = self.split_if_too_long(self.subtitle)
            for st in splited_subtitle:
                content.append({
                    "text": st,
                })
        if self.title_space:
            content.append({})
        return content

    def format_footer(self, obj={}):
        content = []
        if not 'footer_loader' in obj:
            return content
        if not 'load_cur' in obj['footer_loader'] or not 'load_max' in obj['footer_loader']:
            raise ValueError("Missing 'load_cur' or 'load_max' in 'loading_bar'.")
        
        bar_length = self.length - 2
        load_cur = obj['footer_loader']['load_cur']
        load_max = obj['footer_loader']['load_max']
        filled_length = int(bar_length * load_cur // load_max)
        colored_filled = self.color_text(
            self.footer_loading_color,
            self.footer_loading_char * filled_length,
            self.footer_loading_bg,
            self.footer_loading_style
        )
        empty_length = bar_length - filled_length
        colored_empty = self.color_text(
            self.footer_loading_empty_color,
            self.footer_loading_empty_char * empty_length,
            self.footer_loading_empty_bg,
            self.footer_loading_empty_style
        )
        if self.footer_loading_reverse:
            text = f"{colored_empty}{colored_filled}"
        else:
            text = f"{colored_filled}{colored_empty}"
        for _ in range(self.footer_loading_thickness):
            content.append({
                "text": text
            })
        return content

    def format_loading_bar(self, loading_bar={}):
        # --- Error handling ---
        if not type(loading_bar) is dict:
            raise ValueError("'loading_bar' must be a dict.")
        if not 'load_cur' in loading_bar or not 'load_max' in loading_bar:
            raise ValueError("Missing 'load_cur' or 'load_max' in 'loading_bar'.")
        # --- Formatting ---
        load_cur = loading_bar['load_cur']
        load_max = loading_bar['load_max']
        filled_length = int(self.loading_bar_length * load_cur // load_max)
        colored_filled = self.color_text(
            self.loading_color,
            self.loading_char * filled_length,
            self.loading_bg,
            self.loading_style
        )
        empty_length = self.loading_bar_length - filled_length
        colored_empty = self.color_text(
            self.loading_empty_color,
            self.loading_empty_char * empty_length,
            self.loading_empty_bg,
            self.loading_empty_style
        )
        colored_opening = self.color_text(
            self.loading_bar_color,
            self.opening_loading_bar_char,
            self.loading_bar_bg,
            self.loading_bar_style
        )
        colored_closing = self.color_text(
            self.loading_bar_color,
            self.closing_loading_bar_char,
            self.loading_bar_bg,
            self.loading_bar_style
        )
        # --- Return ---
        if self.loading_reverse:
            text = f"{colored_opening}{colored_empty}{colored_filled}{colored_closing}"
        else:
            text = f"{colored_opening}{colored_filled}{colored_empty}{colored_closing}"
        return text

    def format_body(self, obj={}):
        content = []
        if not 'body' in obj:
            return content
        
        # --- Padding ---
        def padd_content(content, padding):
            for _ in range(padding):
                content.append({})
            return content

        # --- Body ---
        content = padd_content(content, self.body_padding)
        for line in obj['body']:
            if line == {}:
                content.append({})
            elif 'text' in line:
                splited_text = self.split_if_too_long(line['text'])
                for st in splited_text:
                    content.append({
                        "text": st,
                    })
            elif 'loader' in line:
                text = self.format_loading_bar(line['loader'])
                for _ in range(self.loading_thickness):
                    content.append({
                        "text": text
                    })
            else:
                raise ValueError("Invalid body line.")
        content = padd_content(content, self.body_padding)
        return content

    def format_left_side_bar_loader(
            self, obj={}, title_lines=0, footer_lines=0, body_lines=0
            ):
        if not 'left_side_loader' in obj:
            return {}
        if not 'load_cur' in obj['left_side_loader'] or not 'load_max' in obj['left_side_loader']:
            raise ValueError("Missing 'load_cur' or 'load_max' in 'left_side_loader'.")

        colored_load_char = self.color_text(
            self.left_side_bar_loader_color,
            self.left_side_bar_loader_char * self.left_side_bar_loader_thickness,
            self.left_side_bar_loader_bg,
            self.left_side_bar_loader_style
        )
        colored_empty_char = self.color_text(
            self.left_side_bar_loader_empty_color,
            self.left_side_bar_loader_empty_char * self.left_side_bar_loader_thickness,
            self.left_side_bar_loader_empty_bg,
            self.left_side_bar_loader_empty_style
        )

        if body_lines == 0:
            return {}

        total_high = body_lines
        if self.left_side_bar_loader_on_title:
            total_high += title_lines + 1
        if self.left_side_bar_loader_on_footer:
            total_high += footer_lines + 1

        load_cur = obj['left_side_loader']['load_cur']
        load_max = obj['left_side_loader']['load_max']

        nb_load_lines = int(total_high * load_cur // load_max)
        nb_empty_lines = total_high - nb_load_lines

        if self.left_side_bar_loader_reverse:
            return {
                "load_char": colored_empty_char,
                "empty_char": colored_load_char,
                "nb_load_lines": nb_empty_lines,
                "nb_empty_lines": nb_load_lines
            }

        return {
            "load_char": colored_load_char,
            "empty_char": colored_empty_char,
            "nb_load_lines": nb_load_lines,
            "nb_empty_lines": nb_empty_lines
        }
    
    def format_right_side_bar_loader(
            self, obj={}, title_lines=0, footer_lines=0, body_lines=0
            ):
        if not 'right_side_loader' in obj:
            return {}
        if not 'load_cur' in obj['right_side_loader'] or not 'load_max' in obj['right_side_loader']:
            raise ValueError("Missing 'load_cur' or 'load_max' in 'right_side_loader'.")

        colored_load_char = self.color_text(
            self.right_side_bar_loader_color,
            self.right_side_bar_loader_char * self.right_side_bar_loader_thickness,
            self.right_side_bar_loader_bg,
            self.right_side_bar_loader_style
        )
        colored_empty_char = self.color_text(
            self.right_side_bar_loader_empty_color,
            self.right_side_bar_loader_empty_char * self.right_side_bar_loader_thickness,
            self.right_side_bar_loader_empty_bg,
            self.right_side_bar_loader_empty_style
        )

        if body_lines == 0:
            return {}

        total_high = body_lines
        if self.right_side_bar_loader_on_title:
            total_high += title_lines + 1
        if self.right_side_bar_loader_on_footer:
            total_high += footer_lines + 1

        load_cur = obj['right_side_loader']['load_cur']
        load_max = obj['right_side_loader']['load_max']

        nb_load_lines = int(total_high * load_cur // load_max)
        nb_empty_lines = total_high - nb_load_lines

        if self.right_side_bar_loader_reverse:
            return {
                "load_char": colored_empty_char,
                "empty_char": colored_load_char,
                "nb_load_lines": nb_empty_lines,
                "nb_empty_lines": nb_load_lines
            }

        return {
            "load_char": colored_load_char,
            "empty_char": colored_empty_char,
            "nb_load_lines": nb_load_lines,
            "nb_empty_lines": nb_empty_lines
        }
        
    def from_obj_to_formatted(self, obj):
        formatted_obj = {
            "title": {},
            "body": {},
            "footer": {},
            "left_side_bar_loader": {},
            "right_side_bar_loader": {}
        }

        # --- Title ---
        formatted_obj['title']['content'] = self.format_title(obj)
        formatted_obj['title']['nb_lines'] = len(formatted_obj['title']['content'])

        # --- Body ---
        formatted_obj['body']['content'] = self.format_body(obj)
        formatted_obj['body']['nb_lines'] = len(formatted_obj['body']['content'])

        # --- Footer ---
        formatted_obj['footer']['content'] = self.format_footer(obj)
        formatted_obj['footer']['nb_lines'] = len(formatted_obj['footer']['content'])

        # --- Left side bar loader ---
        formatted_obj['left_side_bar_loader'] = self.format_left_side_bar_loader(
            obj=obj,
            title_lines=formatted_obj['title']['nb_lines'],
            footer_lines=formatted_obj['footer']['nb_lines'],
            body_lines=formatted_obj['body']['nb_lines']
        )
        
        # --- Right side bar loader ---
        formatted_obj['right_side_bar_loader'] = self.format_right_side_bar_loader(
            obj=obj,
            title_lines=formatted_obj['title']['nb_lines'],
            footer_lines=formatted_obj['footer']['nb_lines'],
            body_lines=formatted_obj['body']['nb_lines']
        )

        return formatted_obj
    
    def print_text(self, text, left_cased=False, right_cased=False, end=""):
        text_color_length = self.calculate_color_length(text)
        padding = self.body_padding * 2
        max_length = self.length - padding
        padding = " " * self.body_padding
        case_color = self.color_text(
            self.case_color,
            self.case_char,
            self.case_bg,
            self.case_style
        )
        left, right = "", ""
        if left_cased:
            left = case_color
            max_length -= 1
        if right_cased:
            right = case_color
            max_length -= 1
        centered_text = f"{text.center(max_length + text_color_length)}"
        print(f"{left}{padding}{centered_text}{padding}{right}", end=end)


    def print_margin(self, side=False, end=""):
        if side:
            print(" "*self.margin, end=end)
            return
        for _ in range(self.margin):
            print()

    def print_left_side_bar_loader(self, obj, part=""):
        if obj['left_side_bar_loader'] == {}:
            return
        if part not in ["full", "space", "load_empty"]:
            raise ValueError("Invalid part for the left side bar loader, should be 'full', 'space' or 'load_empty'.")
        if part == "space":
            print(" " * (self.left_side_bar_loader_thickness + 1), end="")
            return
        if part == "full":
            colored_cases = self.color_text(
                self.case_color,
                self.case_char * (self.left_side_bar_loader_thickness + 1),
                self.case_bg,
                self.case_style
            )
            print(colored_cases, end="")
            return
        loader = obj['left_side_bar_loader']
        colored_case = self.color_text(
            self.case_color,
            self.case_char,
            self.case_bg,
            self.case_style
        )
        print(f"{colored_case}{loader['load_char'] if loader['nb_load_lines'] > 0 else loader['empty_char']}", end="")
        loader['nb_load_lines'] -= 1

    def print_right_side_bar_loader(self, obj, part=""):
        if obj['right_side_bar_loader'] == {}:
            return
        if part not in ["full", "space", "load_empty"]:
            raise ValueError("Invalid part for the right side bar loader, should be 'full', 'space' or 'load_empty'.")
        if part == "space":
            print(" " * (self.right_side_bar_loader_thickness + 1), end="")
            return
        if part == "full":
            colored_cases = self.color_text(
                self.case_color,
                self.case_char * (self.right_side_bar_loader_thickness + 1),
                self.case_bg,
                self.case_style
            )
            print(colored_cases, end="")
            return
        loader = obj['right_side_bar_loader']
        colored_case = self.color_text(
            self.case_color,
            self.case_char,
            self.case_bg,
            self.case_style
        )
        print(f"{loader['load_char'] if loader['nb_load_lines'] > 0 else loader['empty_char']}{colored_case}", end="")
        loader['nb_load_lines'] -= 1

    def print_title(self, obj):
        title = obj['title']
        # --- Create the full line separator ---
        full_line = self.color_text(
            self.case_color,
            self.case_char * self.length,
            self.case_bg,
            self.case_style
        )

        # --- Left and Right cased ---
        isLeftCased = self.is_case or (obj['left_side_bar_loader'] != {} and self.left_side_bar_loader_on_title)
        isRightCased = self.is_case or (obj['right_side_bar_loader'] != {} and self.right_side_bar_loader_on_title)
        # --- Print the full bar ---
        self.print_margin(side=True)
        left_part = "full" if self.left_side_bar_loader_on_title else "space"
        self.print_left_side_bar_loader(obj, part=left_part)
        print(full_line, end="")
        right_part = "full" if self.right_side_bar_loader_on_title else "space"
        self.print_right_side_bar_loader(obj, part=right_part)
        self.print_margin(side=True, end="\n")

        # --- Print the title ---
        if left_part == "full":
            left_part = "load_empty"
        if right_part == "full":
            right_part = "load_empty"

        for line in title['content']:
            if line == {}:
                self.print_margin(side=True)
                self.print_left_side_bar_loader(obj, part=left_part)
                self.print_text("", end="", left_cased=isLeftCased, right_cased=isRightCased)
                self.print_right_side_bar_loader(obj, part=right_part)
            elif 'text' in line:
                self.print_margin(side=True)
                self.print_left_side_bar_loader(obj, part=left_part)
                self.print_text(line['text'], end="", left_cased=isLeftCased, right_cased=isRightCased)
                self.print_right_side_bar_loader(obj, part=right_part)
            else:
                raise ValueError("Invalid title line.")
            self.print_margin(side=True, end="\n")
        
        # --- Print the full bar ---
        if left_part == "space":
            left_part = "full"
        if right_part == "space":
            right_part = "full"
        self.print_margin(side=True)
        self.print_left_side_bar_loader(obj, part=left_part)
        print(full_line, end="")
        self.print_right_side_bar_loader(obj, part=right_part)
        self.print_margin(side=True, end="\n")

    def print_body(self, obj):
        if not 'body' in obj:
            return
        body = obj['body']

        isLeftCased = self.is_case or (obj['left_side_bar_loader'] != {})
        isRightCased = self.is_case or (obj['right_side_bar_loader'] != {})
        
        for content in body['content']:
            if content == {}:
                text = ""
            else:
                text = content['text']
            self.print_margin(side=True)
            self.print_left_side_bar_loader(obj, part="load_empty")
            self.print_text(text, end="", left_cased=isLeftCased, right_cased=isRightCased)
            self.print_right_side_bar_loader(obj, part="load_empty")
            self.print_margin(side=True, end="\n")

    def print_footer(self, obj):
        if not 'footer' in obj:
            return
        footer = obj['footer']

        # --- Create the full line separator ---
        full_line = self.color_text(
            self.case_color,
            self.case_char * self.length,
            self.case_bg,
            self.case_style
        )

        # --- Print the full bar ---
        left_part = "full" if not self.left_side_bar_loader_on_footer else "load_empty"
        right_part = "full" if not self.right_side_bar_loader_on_footer else "load_empty"
        if self.is_case and footer['nb_lines'] == 0:
            left_part, right_part = "full", "full"
        self.print_margin(side=True)
        self.print_left_side_bar_loader(obj, part=left_part)
        if self.is_case or footer['nb_lines'] != 0:
            print(full_line, end="")
        else:
            print(" " * self.length, end="")
        self.print_right_side_bar_loader(obj, part=right_part)
        self.print_margin(side=True, end="\n")

        # --- Print the footer ---
        if left_part == "full":
            left_part = "space"
        if right_part == "full":
            right_part = "space"
        if footer['nb_lines'] == 0:
            return
        case_char = self.color_text(
            self.case_color,
            self.case_char,
            self.case_bg,
            self.case_style
        )
        for content in footer['content']:
            if content == {}:
                text = ""
            else:
                text = content['text']
            self.print_margin(side=True)
            self.print_left_side_bar_loader(obj, part=left_part)
            # print(len(text) - self.calculate_color_length(text))
            print(f"{case_char}{text}{case_char}", end="")
            self.print_right_side_bar_loader(obj, part=right_part)
            self.print_margin(side=True, end="\n")

        # --- Print the full bar ---
        if left_part == "load_empty":
            left_part = "full"
        if right_part == "load_empty":
            right_part = "full"
        self.print_margin(side=True)
        self.print_left_side_bar_loader(obj, part=left_part)
        print(full_line, end="")
        self.print_right_side_bar_loader(obj, part=right_part)
        self.print_margin(side=True, end="\n")


    def display_obj(self, obj={}, clear_console=True):
        """
        Display the object that will be formatted in the console.

        Args:
            obj (dict): The object to be displayed. Must be a dictionary.
            clear_console (bool): Whether to clear the console before displaying the object.

        Raises:
            ValueError: If the 'obj' parameter is not a dictionary.
        """
        if not type(obj) is dict:
            raise ValueError("'obj' must be a dict.")
        
        if self.is_already_printing:
            return
        self.is_already_printing = True
        if clear_console:
            self.clear_console()

        formatted_obj = self.from_obj_to_formatted(obj)
        
        # --- Up Margin ---
        self.print_margin()

        # --- Title ---
        self.print_title(formatted_obj)
        # --- Body ---
        self.print_body(formatted_obj)
        # --- Footer ---
        self.print_footer(formatted_obj)
        # --- Down Margin ---
        self.print_margin()

        self.is_already_printing = False
