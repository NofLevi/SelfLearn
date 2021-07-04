import FuncFile
def main():
    func = FuncFile.Functions
    print("Selenium Functions:" + "\n" + 
          "1.Title and SourceCode" + "\n" +
          "2.BMI Calculator [Locators Example]" + "\n" +
          "3.DropDownMenu Example" + "\n" +
          "4.Verification Example",)
    
    switch = input();
    result = {
        '1': lambda: func.title_and_source(),
        '2': lambda: func.locators(),
        '3': lambda: func.drop_down_menu(),
        '4': lambda: func.verification(),
        }[switch]()

if __name__ == "__main__":
    main()
