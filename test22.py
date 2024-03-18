import re

def replace_languages_with_yaml(input_string):
    replacements = {
        'groovy': '  language: groovy',
        'hcl': '  language: hcl',
        'node': '  language: node'
    }
    
    # Regular expression pattern to match words
    pattern = re.compile(r'\b(' + '|'.join(re.escape(key) for key in replacements.keys()) + r')\b', re.IGNORECASE)
    
    # Replace matching words with YAML representation
    output_string = pattern.sub(lambda x: replacements[x.group().lower()], input_string)
    
    return output_string

# Example usage:
input_string = "This is a Groovy script, and here is some HCL and Node code."
output_string = replace_languages_with_yaml(input_string)
print(output_string)
