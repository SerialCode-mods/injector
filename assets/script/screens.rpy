screen preferences():
    tag menu

    if main_menu:
        if persistent.main_menu_wallpaper == 2:
            add "menu_movie2"
            add "gui/darken75.png"
        elif persistent.main_menu_wallpaper == 1:
            add "menu_movie"
            add "gui/darken75.png"
    else:
        add "gui/darken50.png"
        add "gui/min_frame.png"

    use game_menu(_(""), scroll="viewport"):
        vbox:
            xpos 0
            ypos -20
            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):
                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))
                        
                vbox:
                    style_prefix "check"
                    label _("Quick Menu")
                    null width 5  # Left some space to aerate.
                    textbutton "On":
                        tooltip "Show Ren'Py quick menu on the bottom of the textbox. (Disabled by default, interferes with UI)"
                        # Decide when the button is to be shown as /selected/.
                        selected persistent.quick_menu
                        action SetField( persistent, "quick_menu", True )
                    null width 5  # Left some space to aerate.
                    textbutton "Off":
                        tooltip "Show Ren'Py quick menu on the bottom of the textbox. (Disabled by default, interferes with UI)"
                        # Decide when the button is to be shown as /selected/.
                        selected not persistent.quick_menu
                        action SetField( persistent, "quick_menu", False )

            null height (2 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("Text Speed")
                    bar value Preference("text speed")
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")
                    vbox:
                        label _("Dialogue Box Opacity")
                        bar value FieldValue(persistent, "dialogueBoxOpacity", range=1.0, style="slider") xmaximum 500 tooltip "Maximum opacity may obfuscate some scenes. Text is also optimized to be legible with no textbox."

                vbox:

                    if config.has_music:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

                    if config.has_voice:
                        label _("Voice Volume")
                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

            vbox:
                hbox:
                
                    vbox:
                        style_prefix "check"
                        label _("Menu Parallax")
                        null width 5  # Left some space to aerate.
                        textbutton "On":
                            tooltip "Parallax effect in the menus may be buggy while game is running inside a window, you can disable it here."
                            # Decide when the button is to be shown as /selected/.
                            selected persistent.menu_parallax
                            action SetField( persistent, "menu_parallax", True )
                        null width 5  # Left some space to aerate.
                        textbutton "Off":
                            tooltip "Parallax effect in the menus may be buggy while game is running inside a window, you can disable it here."
                            # Decide when the button is to be shown as /selected/.
                            selected not persistent.menu_parallax
                            action SetField( persistent, "menu_parallax", False )

                    vbox:
                        style_prefix "check"
                        label _("Main Menu")
                        null width 5  # Left some space to aerate.
                        textbutton "Default":
                            tooltip "Default Serial:Code main menu background."
                            # Decide when the button is to be shown as /selected/.
                            action SetField( persistent, "main_menu_wallpaper", 1 )
                        null width 5  # Left some space to aerate.
                        textbutton "Mariko":
                            tooltip "Mariko main menu background."
                            # Decide when the button is to be shown as /selected/.
                            action SetField( persistent, "main_menu_wallpaper", 2 )


                    vbox:
                        style_prefix "check"
                        label _("NTR+")
                        null width 5  # Left some space to aerate.
                        textbutton "On":
                            tooltip "Disables/Enables NTR and NTS content. To have your choice reflected in the {b}gallery{/b}, please restart your game."
                            # Decide when the button is to be shown as /selected/.
                            selected persistent.ntr_switch
                            action SetField( persistent, "ntr_switch", True )
                        null width 5  # Left some space to aerate.
                        textbutton "Off":
                            tooltip "Disables/Enables NTR and NTS content. To have your choice reflected in the {b}gallery{/b}, please restart your game."
                            # Decide when the button is to be shown as /selected/.
                            selected not persistent.ntr_switch
                            action SetField( persistent, "ntr_switch", False )

                    vbox:
                        style_prefix "small_button"
                        label _("Modloader")
                        null width 5  # Left some space to aerate.
                        textbutton "Open Modloader":
                            tooltip "Opens the Modloader menu."
                            # Decide when the button is to be shown as /selected/.
                            action ShowMenu("injector_options")


                yoffset 0
            
    $ tooltip = GetTooltip()

    if tooltip:
        text "[tooltip]":
            xalign 0.5
            yalign 0.1


    text "{color=#09CB97} Settings {/color}" font "fonts/CYGUN-Regular.otf" xoffset 50 yoffset 8
    # add "gui/upper_buttons.png" xoffset 284 yoffset 30
    add "gui/min_frame.png"
