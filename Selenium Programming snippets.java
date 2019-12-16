import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.util.concurrent.TimeUnit;




//Setup Selenium WebDriver Object
WebDriver driver;
System.setProperty("webdriver.chrome.driver", "D:\\Programming materials\\Selenium\\Web Drivers\\chromedriver_win32\\chromedriver.exe");
driver = new ChromeDriver();


//Prerequisites to prepare a browser
driver.manage().deleteAllCookies();
driver.manage().window().maximize();
driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
driver.manage().timeouts().pageLoadTimeout(30, TimeUnit.SECONDS);

//Load a Webpage
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin");

