def helper_clean_list_button():
    sheet = 'QPushButton{background-color: qlineargradient(spread:pad, x1:1, y1:0.074, x2:0, ' \
            'y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));' \
            'border-radius: 10px;padding: 5px;color: rgb(255, 255, 255);font: 14pt \"Courier\";' \
            'border-bottom: 2px outset black;}' \
            'QPushButton:pressed{padding: 1px -1px -1px 1px;border-bottom: 0 inset black;}' \
            'QPushButton:hover{background-color: #4000FF;}'

    return sheet


def helper_search_input_button():
    sheet = "QPushButton{background-color: qlineargradient(spread:pad, x1:1, " \
            "y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));" \
            "border-radius: 10px;" \
            "color: rgb(255, 255, 255);font: 14pt \"Courier\";" \
            "border-bottom: 2px outset black;}" \
            "QPushButton:pressed{padding: 1px -1px -1px 1px;border-bottom: 1px inset black;}" \
            "QPushButton:hover{background-color: #4000FF;}"
    return sheet


def helper_save_list_button():
    return helper_search_input_button()


def helper_open_browser_button():
    return helper_search_input_button()


####################################################################################

def helper_background_mini_browser():
    background = "background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, " \
                 "stop:0 rgba(63, 217, 93, 255), stop:1 rgba(137, 230, 65, 255));}"
    return background


def helper_input_mini_browser():
    background = "background-color: rgb(255, 255, 255);\n" \
                 "font: 12pt \"Courier\";\n" \
                 "border-radius: 12px;\npadding: 12px;"
    return background


def helper_search_mini_browser():
    background = "background-color: qlineargradient(spread:pad, x1:1, " \
                 "y1:0.074, x2:0, y2:0.966227, stop:0 rgba(0, 0, 0, 255), stop:0.9375 rgba(10, 29, 2, 255));" \
                 "border-radius: 10px;color: rgb(255, 255, 255);font: 14pt \"Courier\";" \
                 "border-bottom: 2px outset black;}" \
                 "QPushButton:pressed{padding: 1px -1px -1px 1px;border-bottom: 1px inset black;}" \
                 "QPushButton:hover{background-color: #4000FF;"
    return background
