
class OutputHandler:
    def __init__(self, mode = 'standard'):
        valid_modes = ['standard', 'dev']
        if mode not in valid_modes:
            raise ValueError(f'Invalid mode: {mode}')
        self.mode = mode



    def friendly_output_handler(self, output):
        """
        Takes the output dictionary and makes it readable for user.
        """
        message = []
        if output['found']:
            message.append(f"Here is your text in UTF-8: {output['found']}")
        if output['non_found']:
            message.append(f"Here are the elements that could not be"
                       f" found and their index number: {dict(output['non_found'])}")
        new_line = '\n'.join(message)
        return new_line