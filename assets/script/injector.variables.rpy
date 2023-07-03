init python:
    def register(func):
        """Automatically register functions
        Args:
            func (function):
                The function to register
        """
        # If not a function, raise an error
        if not hasattr(func, '__call__'):
            raise ValueError('You need to specify a function to add to register into the injector\'s api')
        else:
            # Register the given function
            injector[func.__name__] = func

    def jump_both_label_callback(name, jump):
        renpy.jump()

    def jump_both(custom, original):
        """Jump to both the original and custom label

        Args:
            custom (str):
                The label which will have to be jumped or called
            original (str):
                The original label which will have to be jumped or called
        """        
        jump_both_original_label_callback = config.label_callback

    def filter_scripts(scripts: [str]):
        """Filter the given list of scripts
        Args:
            scripts (list):
                The list of script that need to be filtered
            extension (str):
                The extension to use to filter. Not passing an argument will
                make it catch every file that fits the
                `^([a-z0-9]{3,15})\\.rpy$` regex
        Returns:
            {
                enabled (list):
                    Mods to enable on load
                disabled (list):
                    Mods to ignore
            }
        """
        from re import compile

        regex = compile(
            '^([a-z0-9]{3,15})' + '\\.mod\\.rpy$'
        )

        scripts = filter(
            lambda s: regex.match(s) != 'injector',
            scripts
        )
        
        temp_s = {
            'enabled': [],
            'disabled': [],
            'all': []
        }

        for s in scripts:
            # Get mod's name to avoid conflicts betwween files
            namespace = regex.match(s).group(1)

            # Sort mods
            temp_s['disabled' if namespace in injector_config['mods']['disabled'] else 'enabled'].append(namespace)

            temp_s['all'] = temp_s['enabled'] + temp_s['disabled']
            temp_s['all'].sort()

        # Return filtered list
        return temp_s

    def load_mod(mod: str, label = ''):
        """Live load a mod
        Args:
            mod (str):
                The name of the mod to load
        Returns:
            None
        """
        init_label = mod + label

        if not renpy.has_label(init_label):
            return

        # `renpy.call` will only load the first mod in the list
        renpy.call_in_new_context(init_label)

        # Show the mod as loaded
        loaded.append(mod)

        return

    def enable_mod(mod: str):
        """Enables a mod
        Args:
            mod (str):
                The name of the mod to enable
        Returns:
            None
        """
        mods_config = injector_config['mods']

        if mod not in mods_config['disabled']:
            return

        try:
            # Remove it from the disabled part
            mods_config['disabled'].remove(mod)
            mods_config['disabled'].sort()
            load_mod(mod, '.prepare')
            load_mod(mod, '.load')
            load_mod(mod, '.after')
        except ValueError:
            return

        injector_config['mods'] = mods_config
        write_config(injector_config)
        # renpy.retain_after_load()
        # renpy.reload_script()

    def unload_mod(mod: str):
        """Live unload a mod
        Args:
            mod (str):
                The name of the mod to unload
            label:
                Which part of the mod must be unloaded
        Returns:
            None
        """
        unload_label = f'{mod}.unload'

        if not renpy.has_label(unload_label):
            return

        # `renpy.call` will only load the first mod in the list
        renpy.call_in_new_context(unload_label)

        # Show the mod as unloaded
        loaded.remove(mod)

    def disable_mod(mod: str):
        """Disables a mod
        Args:
            mod (str):
                The name of the mod to enable
        Returns:
            None
        """
        mods_config = injector_config['mods']

        if mod in mods_config['disabled']:
            return

        try:
            # Remove it from the disabled part
            mods_config['disabled'].append(mod)
            mods_config['disabled'].sort()
            unload_mod(mod)
        except ValueError:
            return

        injector_config['mods'] = mods_config
        write_config(injector_config)
        # renpy.retain_after_load()
        # renpy.reload_script()

    def write_config(config_object: dict):
        """Write to the config file
        Args:
            config_object (dict):
                The dictionary of the config.
        """
        from json import dumps

        c_o = open_config('wt')
        c_o.write(dumps(config_object, indent=2))
        c_o.close()

        return

label injector_variables:
    default injector =  {
        'register': register,
        'filter_scripts': filter_scripts,
        'loaded': [],
        'load_mod': load_mod,
        'unload_mod': unload_mod,
        'disable_mod': disable_mod,
        'enable_mod': enable_mod,
        'write_config': write_config
    }

    return
