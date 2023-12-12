# PLEASE DON'T CHANGE THE CODE UNLESS YOU'RE FAMILIAR WITH PROGRAMMING. IT MIGHT CAUSE ERRORS OTHERWISE.
# CHECK IMPORTANT MODULES
try:
    import pandas
    print("pandas was found")
except ImportError:
    print("pandas was not found please install it")
try:
    import sweetviz
    print("Sweetviz was found")
except ImportError:
    print("Sweetviz was not found please install it")

# IMPORT IMPORTANT MODULES
import pandas as pd
import sweetviz as sv

# DEFINE FUNCTIONS
def get_csv():
    return input("Enter your CSV file path or name: ")
    
def get_output():
    while True:
        output = input("Enter name where you want to save: ")
        if output.lower().endswith('.html'):
            return output
        else:
            print("Please enter name with .html at the end")

# PROCESS THE CODE
df = pd.read_csv(get_csv())
print(df)

report = sv.analyze(df)
output_path = get_output() or 'result.html'

report.show_html(output_path)