import settings

def get_colors(specify=False):
    """
    Returns 'button_color',frame_color', 'root_color', 'hover_color', and if custom theme, opacity
    """
    if specify==False:
        current_theme = settings.get_setting("theme")
    else:
        current_theme = specify.lower()
    if current_theme == "red": return {"button_color":"#1a0000","frame_color":"#330000", "root_color":"#1a0000","hover_color":"#3d0101"}
    if current_theme == "green": return {"button_color":"#254B0F","frame_color":"#142C06","root_color":"#0E1F04","hover_color":"#48911d"}
    if current_theme == "blue": return {"button_color":"#00131a","frame_color":"#002533", "root_color":"#00131a","hover_color":"#013245"}
    if current_theme == "purple": return {"button_color":"#1a001a","frame_color":"#330033", "root_color":"#1a001a","hover_color":"#4d004d"}
    if current_theme == "custom":
        theme_attributes: dict = settings.get_custom_theme()
        return theme_attributes
