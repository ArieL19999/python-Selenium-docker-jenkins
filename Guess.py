
    
  def __init__(self, difficulty) -> None:
    self.difficulty = int(difficulty)
    self.match = False
    
  def generate_number(self):  
    self.secret_number = random.randrange(1, self.difficulty + 1) 
    print(f"Generate a secret number equals to: {self.secret_number}")
  
  def get_guess_from_user(self):  
    # generate number between 1 to difficulty and save it to secret_number.        
    self.user_guess = int(input("PLease enter your guessed number: "))
    print(f"Got the number {self.user_guess} from the user")
  
  def compare_results(self):
    print(f"Comparing secret number {self.secret_number} with user input {self.user_guess}")
    if self.secret_number == self.user_guess:
      self.match = True
      
  def play(self):  
    self.generate_number()
    self.get_guess_from_user()
    self.compare_results()
    
    if self.match == True:
      print("\n========================================")
      print(f"We got a winner!!!\n Our secret number {self.secret_number} is equal to your guessed number {self.user_guess}")
      print("========================================\n")
    else:
      print("Nop, you missed it. This is not the chosen number")
            
def main(difficulty):
  game1 = Guess_Game(difficulty)
  game1.play()  

if __name__ == "__main__":
  main()
