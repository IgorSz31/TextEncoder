
class OutputHandler:
    def __init__(self, mode = 'standard'):
        valid_modes = ['standard', 'dev']
        if mode not in valid_modes:
            raise ValueError(f'Invalid mode: {mode}')
        self.mode = mode


    def handle_empty_input(self):
        print('a')
        return 'String cant be empty'
