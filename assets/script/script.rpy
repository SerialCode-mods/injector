# Init mods
init -1 python:
    from json import load,dumps
    from os import path
    # from os import listdir
    from glob import glob
    import datetime
    import itertools

    def open_config(mode = 'rt'):
        return open(os.path.dirname(os.path.realpath(__file__)) + '/../' + 'injector_config.json', mode)

    try:
        open_config()
    except IOError:
        open_config('wt').write(dumps({
            'mods': {
                'disabled': []
            }
        }, indent=2))
    finally:
        injector_config = load(open_config())

    loaded = []
    mods = None

    # Backup the label_callback for possible later use
    original_label_callback = config.label_callback

    def path_to_basename(file):
        return path.basename(file)

    # Dirty trick
    def injector_label_callback(name, abnormal):
        """Custom label_callback made to inject the mod when splashscreen launches
        Args:
            name (str):
                The name of the label
            abnormal (bool):
                If it was reached through jump, call or by creating a new
                context
        """
        labels = {
            'before_main_menu': '.before',
            'main_menu_screen': '.prepare',
            'start': '.after',
            'after_load': '.after'
        }

        # Inject at splashscreen, load mods or return otherwise
        if name == 'splashscreen':
            renpy.call('injector_variables')
        elif name in labels:
            global mods
            mods = injector['filter_scripts'](list(map(path_to_basename, glob('./game/mods/**/*.mod.rpy'))))

            for mod in mods['enabled']:
                label = labels[name]
                injector['load_mod'](mod, label)

    # Use custom callback to inject
    config.label_callback = injector_label_callback
