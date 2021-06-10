from faker import Faker

fake = Faker()

def get_text():
    return {
        "text": fake.text()
    }

if __name__ == '__main__':
    print(get_text())