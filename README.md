# SOS_Game_Algorithm
1.Take the names of the two players
2. Shuffle the two players to choose randomly who will start
3. Design the board of 4x4
4. Display board to both players with player 1 score equal zero and player 2 score equal zero
5. counter = 0
6. While (counter not equal to 16)
	7. Take player one input as “S” or “O”
	8. Increment counter by 1
	9. If SOS pattern is formed in board
		9a. Increment player one score by 1
	10. Take player two input as “S” or “O”
	11. Increment counter by 1
	12. If SOS pattern is formed in board
		12a. Increment player two score by 1
	13. If counter equals 16
		13a. Stop
14. If player 1 score greater than player 2 score
	14a. Output (“Player one is the winner!”)
	14b. Stop
15. If player 2 score greater than player 1 score
15a. Output (“Player two is the winner!”)
15b. Stop
16. If player 1 score equals player 2 score
	16a. Output (“Game is draw!”)
	16b. Stop
