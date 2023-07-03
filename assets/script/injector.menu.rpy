screen injector_options():
    $ import itertools

    add "gui/darken50.png"

    tag menu
    use game_menu(_('Injector options'), scroll='viewport'):
        vbox:
            hbox:
                box_wrap True
                for mod in mods['all']:
                    vbox:
                        style_prefix 'radio'
                        label _(mod.capitalize())
                        textbutton _('Enable') action [
                            SetVariable('persistent.injector_mods_' + mod, 1),
                            Function(injector['enable_mod'], mod)
                        ]
                        textbutton _('Disable') action [
                            SetVariable('persistent.injector_mods_' + mod, 0),
                            Function(injector['disable_mod'], mod)
                        ]

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

screen gameUI():
    tag GameUIMain
    # add "ui/Upper_Frame.png"
    if AuraLink == 1:
        add "ui/Upper_Frame.png"
    elif AuraLink == 2:
        add "ui/Upper_Frame_Synth.png"
    elif AuraLink == 3:
        add "ui/Upper_Frame_Min.png"
    elif AuraLink == 9:
        add "ui/Upper_Frame_Marikomood.png"
    elif AuraLink == 10:
        add "ui/Upper_Frame_Retro.png"
    elif AuraLink == 11:
        add "ui/Upper_Frame_Contra.png"
    elif AuraLink == 12:
        add "ui/Upper_Frame_purple1.png"
    elif AuraLink == 13:
        add "ui/Upper_Frame_purple2.png"
    elif AuraLink == 81:
        add "ui/Upper_Frame_Visions.png"
    elif AuraLink == 89:
        add "ui/Upper_Frame_CPro.png"
    elif AuraLink == 90:
        if IsInCombat == False:
            add "ui/Upper_Frame_CProOW.png"
        elif IsInCombat == True:
            add "ui/Upper_Frame_CPro.png"  
    elif AuraLink == 91:
        if IsInCombat == False:
            add "ui/Upper_Frame_CProOW2.png"
        elif IsInCombat == True:
            add "ui/Upper_Frame_CPro.png"  

    zorder 50
    hbox:
        spacing 5
        button:
            xsize 31
            ysize 26
            hover_background "ui/statpillact.png"
            idle_background "ui/statpill.png"
            if IsInCombat == False:
                action  ToggleVariable("CombatStatsOverworld", true_value=True, false_value=False)
            elif IsInCombat == True:
                background "ui/statpilldis.png"
                action None

        if AuraLink == 90 and IsInCombat == False:
            text "It's [dayoftheweek], [Time] {image=calblack.png} [day]" font "fonts/Montserrat-SemiBold.ttf" xalign 0.0 yalign 0.0 size 24 color "#161616" outlines [ (absolute(0.1), "#161616", absolute(0), absolute(0)) ]
        else:
            text "It's [dayoftheweek], [Time] {image=cal.png} [day]" font "fonts/Montserrat-SemiBold.ttf" xalign 0.0 yalign 0.0 size 24 color "#cbd9da" outlines [ (absolute(0.7), "#161616", absolute(0), absolute(0)) ]

        text "" font "fonts/Montserrat-SemiBold.ttf" xalign 0.5 yalign 0.0 size 24


    hbox: 
        if CombatStatsOverworld == True and IsInCombat == False:
            hbox:
                button:
                    xsize 91
                    ysize 90
                    background "ui/CombatScreen/head_main.png"
                    text str(sum([strength, intelligence, hacking, fortitude, social, SpecialPowerRank])- 16):
                        yalign 0.3
                        xalign 0.6
                        text_align 0.5
                        font "fonts/CYGUN-Regular.otf"
                        color "#acacac"
                        if (sum([strength, intelligence, hacking, fortitude, social, SpecialPowerRank])- 16) < 100:
                            size 76
                        elif (sum([strength, intelligence, hacking, fortitude, social, SpecialPowerRank])- 16) > 100:
                            size 56    
            
            xalign 0.0
            yalign 0.041
            vbox:
                yoffset 5
                spacing 2
                hbox:
                    bar:
                        left_bar Frame("ui/CombatScreen/hp2_ow.png", 10, 0)
                        right_bar Frame("ui/CombatScreen/hp1_ow.png", 10, 0)
                        xsize 538
                        ysize 40
                        value protag_hp
                        range protag_hp_max
                        left_gutter 0
                        right_gutter 0
                        thumb None
                        thumb_shadow None
                    vbox:
                        xoffset -45
                        text "[protag_hp_max]": 
                            style "hpbaroffow"
                            xoffset 55
                            yoffset 20
                        text "[protag_hp]" style "hpbarow"
                        

                    null width 4
                null height 4

                hbox:
                    yoffset -60
                    grid 30 5:
                        spacing -8
                        allow_underfull True
                        for i in range(protag_tp):
                            add "ui/CombatScreen/battgridon_ow.png"
                        for i in range(protag_tp_max-protag_tp):
                            add "ui/CombatScreen/battgridoff_ow.png"
                        

                    null width 4
                null height 4

                text "Threat Level: Low":
                    style "threatow"
                    yoffset -315
                    xoffset 10

    hbox:
        xalign 0.99
        yalign 0.0
        spacing 20
        imagebutton:
            if AuraLink == 89:
                idle "ui/Files_idle2.png" hover "ui/Files_hover.png"
            elif (AuraLink == 90 or AuraLink == 91) and IsInCombat == True:
                idle "ui/Files_idle2.png" hover "ui/Files_hover.png"    
            else:
                idle "ui/Files_idle.png" hover "ui/Files_hover.png"
            action ShowMenu("category_welcome")

        imagebutton:
            if AuraLink == 89:
                idle "ui/Shards_idle2.png" hover "ui/Shards_hover.png"
            elif (AuraLink == 90 or AuraLink == 91) and IsInCombat == True:
                idle "ui/Shards_idle2.png" hover "ui/Shards_hover.png"
            else:
                idle "ui/Shards_idle.png" hover "ui/Shards_hover.png"
            action ShowMenu("ShardsUI")

        imagebutton:
            if AuraLink == 89:
                idle "ui/Items_idle2.png" hover "ui/Items_hover.png"
            elif (AuraLink == 90 or AuraLink == 91) and IsInCombat == True:
                idle "ui/Items_idle2.png" hover "ui/Items_hover.png"
            else:
                idle "ui/Items_idle.png" hover "ui/Items_hover.png"
            action ShowMenu("ItemsUI")

        imagebutton:
            if AuraLink == 89:
                idle "ui/Stats_idle2.png" hover "ui/Stats_hover.png"
            elif (AuraLink == 90 or AuraLink == 91) and IsInCombat == True:
                idle "ui/Stats_idle2.png" hover "ui/Stats_hover.png"
            else:
                idle "ui/Stats_idle.png" hover "ui/Stats_hover.png"
            action ShowMenu("StatsUI")

        imagebutton auto "mods/injector/images/ui/injector_%s.png" action ShowMenu("injector_options")
        # imagebutton:
        #     if AuraLink == 89:
        #         # idle "mods/injector/images/ui/Stats_idle2.png" hover "mods/injector/ui/_hover.png"
        #         "mods/injector/images/ui/injector_%s.png"
        #     elif (AuraLink == 90 or AuraLink == 91) and IsInCombat == True:
        #         # idle "mods/injector/images/ui/injector_idle2.png" hover "mods/injector/ui/_hover.png"
        #         "mods/injector/images/ui/injector_%s.png"
        #     else:
        #         # idle "mods/injector/images/ui/injector_idle.png" hover "mods/injector/ui/_hover.png"
        #         "mods/injector/images/ui/injector_%s.png"

        #     action ShowMenu("StatsUI")

# screen nav_screen():
#     vbox:
#         xpos 14
#         ypos 17
#         vbox:
#             text "Day [day],\n[date_array[%s]] [Time]" % week_day
#     vbox:
#         xalign 1.0
#         ypos 13
#         hbox:
#             imagebutton auto "gui/button/injector_%s.png" action [ ShowMenu("injector_options")]
#             imagebutton auto "gui/button/powers_%s.png" action [ Hide("nav_screen"), Show("power_screen")]
#             imagebutton auto "gui/button/leads_%s.png" action [ Hide("nav_screen"), Show("lead_screen")]
#             imagebutton auto "gui/button/bag_%s.png" action [ Hide("nav_screen"), Show("inventory_screen")]
#             imagebutton auto "gui/button/stats_%s.png" action [ Hide("nav_screen"), Show("stats_screen") ]
#             if character_cards == 1:  ## Activated at start of Act Two
#                 imagebutton auto "gui/button/girls_%s.png" action [ Hide("nav_screen"), Show("cc_small_screen1") ]
#             imagebutton auto "gui/button/settings_%s.png" action ShowMenu('preferences')
