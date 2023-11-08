import smtplib
import requests
from bs4 import BeautifulSoup

MY_EMAIL = "pythonmailtest2023@gmail.com"
MY_PASSWORD = "lhsq tscb rqsj rcxa"

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,la;q=0.6,es;q=0.5"
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)

if price_as_float < 100:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Churrasqueira controle remoto por apenas R$ {price_as_float}"
    )
