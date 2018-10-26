import random

print ( "WELCOME to ROCK-PAPER-SCISSORS!!!" )
print ( "You are gonna play with Computer Kem!" )
print ( "\nRULES OF THE GAME: \n 1.Rock beats scissors. \n 2.Scissors beats paper. \n 3.Paper beats rock.\nWinner is the one who gets 5 points first! Are You Ready? Let's Start!!!"  )

ans = "y"
u_score=0
c_score=0
while ( ans == "Y" or ans == "y" ) :
	print ( "\n1.Rock  \n2.Scissors  \n3.Paper  \nEnter Your Choice: " )
	user_choice = int( input() )
	 
	if ( user_choice > 3 or user_choice < 1) :
		print ( "Enter a valid choice:( 1 or 2 or 3)" )
		user_choice = int( input() )
		
	if ( user_choice == 1 ) :
		print ( "You chose Rock!" )
	elif ( user_choice == 2 ) :
		print ( "You chose Scissors!" )
	elif ( user_choice == 3) :
		print ( "You chose Paper!" )
	
	print ( "Now, Kem's turn....." )
	comp_choice = random.randint( 1,3 ) 
	
	if ( comp_choice == 1 ) :
		print ( "Kem chose Rock!" )
	elif ( comp_choice == 2 ) :
		print ( "Kem chose Scissors!" )
	elif ( comp_choice == 3) :
		print ( "Kem chose Paper!" )
		
	if ( comp_choice == user_choice ):
		print ( "It's a tie!")
		print ( "You: ", u_score)
		print ( "Kem: ", c_score)
	elif ( comp_choice == 1 and user_choice == 2 ) :
		print ( "Rock beats scissors! Kem scores a point!" )
		c_score += 1
		print ( "You: ", u_score)
		print ( "Kem: ", c_score)
	elif ( comp_choice == 1 and user_choice == 3 ) :
		print ( "Paper beats rock! You score a point!" )
		u_score += 1
		print ( "You: ", u_score)
		print ( "Kem: ", c_score)
	elif ( comp_choice == 2 and user_choice == 1 ) :
		print ( "Rock beats scissors! You score a point!" )
		u_score += 1
		print ( "You: ", u_score)
		print ( "Kem: ", c_score)
	elif ( comp_choice == 2 and user_choice == 3 ) :
		print ( "Scissors beat paper! Kem scores a point!" )
		c_score += 1
		print ( "You: ", u_score)
		print ( "Kem: ", c_score)
	elif ( comp_choice == 3 and user_choice == 1 ) :
		print ( "Paper beats rock! Kem gets a point!" )
		c_score += 1
		print ( "You: ", u_score)
		print ( "Kem: ", c_score)
	elif ( comp_choice == 3 and user_choice == 2 ) :
		print ( "Scissors beat paper! You get a point!" )
		u_score += 1
		print ( "You: ", u_score)
		print ( "Kem: ", c_score)
	
	if ( u_score == 5 ) : 
		print ( "YOU WIN!!! CONGRATULATIONS!!!" )
		print (" NEW GAME?" )
		print ( "Do you want to play another game?(Y/N) ")
		ans = input()
		u_score=0
		c_score=0
	elif ( c_score == 5 ) :
		print ( "KEM WINS THE GAME!!! BETTER LUCK NEXT TIME!" )
		print (" GAME OVER!" )
		print ( "Do you want to play another game?(Y/N) ")
		ans = input()
		u_score=0
		c_score=0
	else :
		print ( "Do you want to continue? (Y/N): " )
		ans = input()

print ( "THANKS FOR PLAYING!!!" )	
	
