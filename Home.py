import streamlit as st

# Title of the dashboard
st.title("Chess Piece Classification")
st.header("ResNet-50 for Chess Piece Classification")

# Add an image
image = st.image('./image/chess.jpg')

# Introduction to the dashboard's purpose
st.write("""
Welcome to the Chess Piece Classification Dashboard! This application uses a deep learning model based on ResNet-50 to classify images of chess pieces. You can take a picture of a chess piece with your camera, and the model will predict whether it's a King, Queen, Rook, Bishop, Knight, or Pawn.

This model is designed to help beginners and enthusiasts quickly identify chess pieces, and it showcases the power of image classification with convolutional neural networks.
""")

# Brief explanation of what chess is
st.subheader("About Chess")
st.write("""
Chess is a classic strategy board game played by millions around the world. Originating in India, chess involves two players, each controlling an army of pieces with the objective of checkmating the opponent’s king. It requires strategic thinking, planning, and foresight.

Each player has 16 pieces: 1 King, 1 Queen, 2 Rooks, 2 Bishops, 2 Knights, and 8 Pawns. Each piece has unique movement rules, adding complexity to the game.
""")

# Explanation of each chess piece
st.subheader("Chess Pieces and Their Roles")

# King
st.write("**King**")
st.write("""
The King is the most important piece in chess. If the King is checkmated, the game ends. The King moves one square in any direction.
""")

# Queen
st.write("**Queen**")
st.write("""
The Queen is the most powerful piece, able to move any number of squares in any direction—horizontally, vertically, or diagonally.
""")

# Rook
st.write("**Rook**")
st.write("""
The Rook moves in a straight line either horizontally or vertically across the board. Each player has two Rooks, positioned at the corners of the board.
""")

# Bishop
st.write("**Bishop**")
st.write("""
Bishops move diagonally across the board. Each player has two Bishops, one moving on dark squares and the other on light squares.
""")

# Knight
st.write("**Knight**")
st.write("""
Knights move in an "L" shape: two squares in one direction and one square perpendicular. They are the only pieces that can jump over others.
""")

# Pawn
st.write("**Pawn**")
st.write("""
Pawns move forward one square but capture diagonally. They can move two squares forward on their first move. Pawns also have a unique ability to promote into any other piece (except the King) if they reach the opposite side of the board.
""")

st.write("Feel free to explore the classification feature in the next section and try it with your chess pieces!")
