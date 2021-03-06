import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.Select;

public class Functions {
	
	final String dir = System.getProperty("user.dir");
	
	public void openBrowser() {
		System.setProperty("webdriver.chrome.driver", dir + "\\chromedriver.exe");//setup sem folder and file
		WebDriver driver = new ChromeDriver();// set up object
		driver.manage().window().maximize();//open browser on max size
		
		driver.get("https://ksp.co.il/web/"); //open  specific site
		
		System.out.println("Page title is: " + driver.getTitle());//get page title
		//System.out.println(driver.getPageSource());//get pagesource
			
		driver.navigate().back(); //can nevigate back/forward/refresh
		
		driver.quit();
	}
	
	public void locators() {
		System.setProperty("webdriver.chrome.driver", dir + "\\chromedriver.exe");//setup sem folder and file
		WebDriver driver = new ChromeDriver();// set up object
		driver.manage().window().maximize();//open browser on max size
		
		driver.get("https://www.calculator.net/bmi-calculator.html");
		//Elements options: ID/NAME/CLASSNAME/TAGNAME/LINKTEXT/PARTIALLINKTEXT/XPATH/CSSSELECTOR
		WebElement age = driver.findElement(By.id("cage")); //find element by id
		WebElement height = driver.findElement(By.id("cheightmeter"));
		WebElement weight = driver.findElement(By.name("ckg")); //find element by name
		WebElement button = driver.findElement(By.cssSelector("#content > div.leftinput > div.panel2 > table > tbody > tr > td > table:nth-child(4) > tbody > tr > td > input[type=image]:nth-child(2"));
		
		//Actions on webelements
		try {
			age.clear();
			age.sendKeys("25"); // sending string to the text field 
			Thread.sleep(1000);//need sleep between entering data
			
			height.clear();
			height.sendKeys("175");
			Thread.sleep(1000);
			
			weight.clear();
			weight.sendKeys("100");
			Thread.sleep(1000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
			
		button.click();
		
		
		try {
			Thread.sleep(4000);
		}catch (InterruptedException e) {
			// TODO Auto-generated catch block
		}
		
		
		driver.get("http://echoecho.com/htmlforms11.htm");
		WebElement dropList = driver.findElement(By.name("dropdownmenu"));

		Select DropValue = new Select(dropList); //make drop downmenu list
		DropValue.selectByVisibleText("Milk");//select the string option
		//driver.quit();
	}
	
	public void verfications() {
		System.setProperty("webdriver.chrome.driver", dir + "chromedriver.exe");//setup sem folder and file
		WebDriver driver = new ChromeDriver();// set up object
		driver.manage().window().maximize();//open browser on max size
		driver.get("https://flyff-iblis.com/index.php");
		driver.findElement(By.name("username")).sendKeys("testtest123");
		driver.findElement(By.name("password")).sendKeys("testtest123");
		driver.findElement(By.cssSelector("body > div.bgwrap > div > div.bgfrontwrap > div > div > div.bg-content.shadow > div.column-left > div:nth-child(1) > div.inner-content.text-center > form > button")).click();
		
		WebElement logged = driver.findElement(By.cssSelector("body > div.bgwrap > div > div.bgfrontwrap > div > div > div.bg-content.shadow > div.column-left > div:nth-child(1) > div.inner-content-logged.text-center > a:nth-child(6) "));
		boolean displayed = logged.isDisplayed();
		if(displayed) {
			System.out.println("Element was displayed");
			logged.click();
		}
		
		else {
			System.out.println("Element was not displayed");
		}
		
		boolean enabled = logged.isEnabled();
		if(enabled) {
			System.out.println("Element was enabled");
		}
		else {
			System.out.println("Element was disabled");
		}
		
		System.out.println(logged.getText());
		
		//driver.quit();
	}
}
