import view
import importt
import export


def button_click_first():
    some_str = view.choice()
    if some_str == '0':
        some_guide = importt.guide_im_first()
        view.view_data_im(some_guide)
    if some_str == '1':
        some_guide = export.guide_ex_first()
        view.view_data_ex(some_guide[0], some_guide[1])


def button_click_second():
    some_str = view.choice()
    if some_str == '0':
        some_guide = importt.guide_im_second()
        view.view_data_im(some_guide)
    if some_str == '1':
        some_guide = export.guide_ex_second()
        view.view_data_ex(some_guide[0], some_guide[1])
