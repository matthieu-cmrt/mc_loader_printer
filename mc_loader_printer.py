class MCLoaderPrinter:
    class fg:
        BLACK   = '\033[30m'
        RED     = '\033[31m'
        GREEN   = '\033[32m'
        YELLOW  = '\033[33m'
        BLUE    = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN    = '\033[36m'
        WHITE   = '\033[37m'
        RESET   = '\033[39m'
    
    class bg:
        BLACK   = '\033[40m'
        RED     = '\033[41m'
        GREEN   = '\033[42m'
        YELLOW  = '\033[43m'
        BLUE    = '\033[44m'
        MAGENTA = '\033[45m'
        CYAN    = '\033[46m'
        WHITE   = '\033[47m'
        RESET   = '\033[49m'

    class style:
        BRIGHT    = '\033[1m'
        DIM       = '\033[2m'
        NORMAL    = '\033[22m'
        RESET_ALL = '\033[0m'

    def __init__(self, length=100, is_case=True, case_char="*",
                 case_color=fg.BLUE, case_style="", case_bg="",
                 loading_bar_length=80, case_loading_color=fg.BLUE,
                 case_loading_style="", case_loading_bg="", 
                 case_empty_color=fg.YELLOW, case_empty_style="",
                 case_empty_bg="", loading_char="#", empty_char="-",
                 loading_bar_char="[]", loading_color=fg.GREEN,
                 loading_style="", loading_bg="", empty_color=fg.RED,
                 empty_style="", empty_bg="", loading_bar_color=fg.WHITE,
                 loading_bar_style="", loading_bar_bg="", title_color=fg.YELLOW,
                 title_style="", title_bg="", title_space=False, title="Program",
                 subtitle=""):
        self.length = length

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
        
        self.empty_color = empty_color
        self.empty_style = empty_style
        self.empty_bg = empty_bg
        
        if len(loading_char) != 1:
            raise ValueError("Loading char must be of length 1.")
        self.loading_char = loading_char
        if len(empty_char) != 1:
            raise ValueError("Empty char must be of length 1.")
        self.empty_char = empty_char
        if len(loading_bar_char) != 2:
            raise ValueError("Loading bar char must be of length 2.")
        self.opening_loading_bar_char = loading_bar_char[0]
        self.closing_loading_bar_char = loading_bar_char[1]

        self.title_space = title_space
        if len(title) > length - 2:
            raise ValueError(f"Title is too long for the bar. Title length: {len(title)}, Bar length: {length}")
        self.title = title
        self.subtitle = subtitle
        self.title_color = title_color
        self.title_style = title_style
        self.title_bg = title_bg

        if len(subtitle) > length - 2:
            raise ValueError("Subtitle is too long for the bar.")
        
        self.subtitle = subtitle


    def color_text(self, fg="", text="", bg="", style=""):
        """
        Formats the given text with the specified foreground color, background color, and style.

        Args:
            fg (str): The foreground color.
            text (str): The text to be formatted.
            bg (str, optional): The background color. Defaults to "".
            style (str, optional): The style. Defaults to "".

        Returns:
            str: The formatted text.
        """
        return f"{fg}{bg}{style}{text}{MCLoaderPrinter.style.RESET_ALL}"
    
    # calculate_color_length : if \033[ is in text, then it is a color code
    #                           and should be added to the length
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
        
    
    def print_line(self, text, full_case=False):
        """
        Prints a line of text with optional casing.

        Args:
            text (str): The text to be printed.
            full_case (bool, optional): Whether to print the line with full casing. Defaults to False.
        """
        if full_case:
            print(self.color_text(self.case_color, self.case_char * self.length, self.case_bg, self.case_style))
        else:
            if self.is_case:
                colored_case = self.color_text(self.case_color, self.case_char, self.case_bg, self.case_style)
                text_color_length = self.calculate_color_length(text)
                print(f"{colored_case}{text.center(self.length - 2 + text_color_length, ' ')}{colored_case}")
            else:
                print(text.center(self.length, " "))

    def set_new_subtitle(self, subtitle=""):
        """
        Sets a new subtitle for the bar.

        Args:
            subtitle (str): The new subtitle to set.

        Raises:
            ValueError: If the length of the subtitle is greater than the available space in the bar.

        """
        if len(subtitle) > self.length - 4:
            raise ValueError("Subtitle is too long for the bar.")
        
        self.subtitle = subtitle

    def print_loader(self, load_current=-1, load_end=-1, is_footer=False):
        if load_current < 0 or load_end < 0:
            return
        if load_current > load_end:
            raise ValueError("Current load cannot be greater than the end load.")
        if is_footer:
            bar_length = self.length - 2
        else:
            bar_length = self.loading_bar_length

        filled_length = int(bar_length * load_current // load_end)
        empty_length = bar_length - filled_length
        
        full_bar=""
        if is_footer:
            filled_bar = self.color_text(self.case_loading_color, self.loading_char * filled_length, self.case_loading_bg, self.case_loading_style)
            empty_bar = self.color_text(self.case_empty_color, self.empty_char * empty_length, self.case_empty_bg, self.case_empty_style)
            full_bar = f"{filled_bar}{empty_bar}"
        else:
            filled_bar = self.color_text(self.loading_color, self.loading_char * filled_length, self.loading_bg, self.loading_style)
            empty_bar = self.color_text(self.empty_color, self.empty_char * empty_length, self.empty_bg, self.empty_style)
            open_bar = self.color_text(self.loading_bar_color, self.opening_loading_bar_char, self.loading_bar_bg, self.loading_bar_style)
            close_bar = self.color_text(self.loading_bar_color, self.closing_loading_bar_char, self.loading_bar_bg, self.loading_bar_style)
            full_bar = f"{open_bar}{filled_bar}{empty_bar}{close_bar}"
        self.print_line(full_bar)

    def print_title(self):
        """
        Prints the title and subtitle with proper formatting.
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
        self.print_line("")

    def print_footer(self, load_current=-1, load_end=-1):
        self.print_line("")
        self.print_line("", full_case=True)
        if load_current < 0 or load_end < 0:
            return
        if load_current > load_end:
            raise ValueError("Current load cannot be greater than the end load.")
        self.print_loader(load_current, load_end, is_footer=True)
        self.print_line("", full_case=True)
        print("\n" * 5)




