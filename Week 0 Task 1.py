def decode_moves(moves: str):
  

   moves = moves.replace('"', '')
   return moves.split()


command_string = input()
print(decode_moves(command_string))

