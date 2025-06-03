import tkinter as tk
from tkinter import messagebox, ttk
import random

class SankGameGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("⚓ SANK - Naval Battle Game ⚓")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1e3c72')
        self.root.resizable(False, False)
        
        # Game settings
        self.board_size = 7
        self.num_ships = 4
        self.cell_size = 40
        
        # Game state
        self.reset_game()
        
        # Setup GUI
        self.setup_gui()
        self.new_game()
        
    def reset_game(self):
        """Reset all game variables"""
        self.player_board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.computer_board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.player_ships = []
        self.computer_ships = []
        self.player_shots = set()
        self.computer_shots = set()
        self.game_over = False
        self.current_turn = 'player'
        
    def setup_gui(self):
        """Create the main GUI layout"""
        # Title
        title_frame = tk.Frame(self.root, bg='#1e3c72')
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame, 
            text="⚓ SANK ⚓", 
            font=('Arial', 28, 'bold'),
            fg='#4ecdc4',
            bg='#1e3c72'
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Naval Battle Game",
            font=('Arial', 14),
            fg='white',
            bg='#1e3c72'
        )
        subtitle_label.pack()
        
        # Game boards frame
        boards_frame = tk.Frame(self.root, bg='#1e3c72')
        boards_frame.pack(pady=20)
        
        # Player board
        player_frame = tk.Frame(boards_frame, bg='#1e3c72')
        player_frame.pack(side=tk.LEFT, padx=20)
        
        player_title = tk.Label(
            player_frame,
            text="🛡️ Your Fleet",
            font=('Arial', 16, 'bold'),
            fg='#4ecdc4',
            bg='#1e3c72'
        )
        player_title.pack(pady=(0, 10))
        
        self.player_frame_board = tk.Frame(player_frame, bg='#2c3e50', relief=tk.RAISED, bd=3)
        self.player_frame_board.pack()
        
        # Computer board
        computer_frame = tk.Frame(boards_frame, bg='#1e3c72')
        computer_frame.pack(side=tk.RIGHT, padx=20)
        
        computer_title = tk.Label(
            computer_frame,
            text="🎯 Enemy Waters",
            font=('Arial', 16, 'bold'),
            fg='#e74c3c',
            bg='#1e3c72'
        )
        computer_title.pack(pady=(0, 10))
        
        self.computer_frame_board = tk.Frame(computer_frame, bg='#2c3e50', relief=tk.RAISED, bd=3)
        self.computer_frame_board.pack()
        
        # Status and controls
        status_frame = tk.Frame(self.root, bg='#1e3c72')
        status_frame.pack(pady=20)
        
        self.status_label = tk.Label(
            status_frame,
            text="Welcome to Sank! Click on enemy waters to fire!",
            font=('Arial', 12),
            fg='white',
            bg='#34495e',
            relief=tk.RAISED,
            bd=2,
            padx=20,
            pady=10
        )
        self.status_label.pack(pady=10)
        
        # Control buttons
        controls_frame = tk.Frame(self.root, bg='#1e3c72')
        controls_frame.pack(pady=10)
        
        new_game_btn = tk.Button(
            controls_frame,
            text="🔄 New Game",
            font=('Arial', 12, 'bold'),
            bg='#e74c3c',
            fg='white',
            relief=tk.RAISED,
            bd=3,
            padx=20,
            pady=5,
            command=self.new_game,
            cursor='hand2'
        )
        new_game_btn.pack(side=tk.LEFT, padx=10)
        
        quit_btn = tk.Button(
            controls_frame,
            text="❌ Quit",
            font=('Arial', 12, 'bold'),
            bg='#95a5a6',
            fg='white',
            relief=tk.RAISED,
            bd=3,
            padx=20,
            pady=5,
            command=self.root.quit,
            cursor='hand2'
        )
        quit_btn.pack(side=tk.LEFT, padx=10)
        
        # Legend
        legend_frame = tk.Frame(self.root, bg='#1e3c72')
        legend_frame.pack(pady=10)
        
        legend_title = tk.Label(
            legend_frame,
            text="Legend:",
            font=('Arial', 10, 'bold'),
            fg='white',
            bg='#1e3c72'
        )
        legend_title.pack()
        
        legend_items = tk.Frame(legend_frame, bg='#1e3c72')
        legend_items.pack()
        
        legends = [
            ("🚢 Ship", "#27ae60"),
            ("💥 Hit", "#e74c3c"),
            ("💧 Miss", "#95a5a6"),
            ("⬜ Unknown", "#34495e")
        ]
        
        for text, color in legends:
            item_frame = tk.Frame(legend_items, bg='#1e3c72')
            item_frame.pack(side=tk.LEFT, padx=10)
            
            color_box = tk.Label(
                item_frame,
                text="  ",
                bg=color,
                relief=tk.RAISED,
                bd=1
            )
            color_box.pack(side=tk.LEFT)
            
            text_label = tk.Label(
                item_frame,
                text=text,
                font=('Arial', 9),
                fg='white',
                bg='#1e3c72'
            )
            text_label.pack(side=tk.LEFT, padx=(5, 0))
    
    def create_board(self, parent_frame, is_player_board=False):
        """Create a game board with buttons"""
        # Clear existing widgets
        for widget in parent_frame.winfo_children():
            widget.destroy()
            
        buttons = []
        
        # Create header row with column numbers
        header_label = tk.Label(
            parent_frame, text="", width=3, height=2,
            bg='#2c3e50', fg='white', font=('Arial', 10, 'bold')
        )
        header_label.grid(row=0, column=0, padx=1, pady=1)
        
        for col in range(self.board_size):
            col_label = tk.Label(
                parent_frame, text=str(col), width=3, height=2,
                bg='#2c3e50', fg='white', font=('Arial', 10, 'bold')
            )
            col_label.grid(row=0, column=col+1, padx=1, pady=1)
        
        # Create board rows
        for row in range(self.board_size):
            button_row = []
            
            # Row header with row number
            row_label = tk.Label(
                parent_frame, text=str(row), width=3, height=2,
                bg='#2c3e50', fg='white', font=('Arial', 10, 'bold')
            )
            row_label.grid(row=row+1, column=0, padx=1, pady=1)
            
            for col in range(self.board_size):
                btn = tk.Button(
                    parent_frame,
                    text="",
                    width=3,
                    height=2,
                    font=('Arial', 12, 'bold'),
                    bg='#34495e',
                    fg='white',
                    relief=tk.RAISED,
                    bd=2
                )
                
                if not is_player_board:
                    btn.configure(
                        command=lambda r=row, c=col: self.player_shoot(r, c),
                        cursor='crosshair'
                    )
                else:
                    btn.configure(state=tk.DISABLED, cursor='arrow')
                
                btn.grid(row=row+1, column=col+1, padx=1, pady=1)
                button_row.append(btn)
            
            buttons.append(button_row)
        
        return buttons
    
    def place_ships(self, board, ships_list):
        """Place ships randomly on the board"""
        for _ in range(self.num_ships):
            while True:
                orientation = random.choice(['horizontal', 'vertical'])
                
                if orientation == 'horizontal':
                    row = random.randint(0, self.board_size - 1)
                    col = random.randint(0, self.board_size - self.num_ships)
                    ship = [(row, col + i) for i in range(self.num_ships)]
                else:
                    row = random.randint(0, self.board_size - self.num_ships)
                    col = random.randint(0, self.board_size - 1)
                    ship = [(row + i, col) for i in range(self.num_ships)]
                
                if all(board[r][c] == ' ' for r, c in ship):
                    for r, c in ship:
                        board[r][c] = 'S'
                    ships_list.extend(ship)
                    break
    
    def update_board_display(self, buttons, board, hide_ships=True):
        """Update the visual display of a board"""
        for row in range(self.board_size):
            for col in range(self.board_size):
                cell_value = board[row][col]
                btn = buttons[row][col]
                
                if cell_value == 'S' and not hide_ships:
                    btn.configure(text="🚢", bg='#27ae60', fg='white')
                elif cell_value == 'X':
                    btn.configure(text="💥", bg='#e74c3c', fg='white')
                elif cell_value == 'O':
                    btn.configure(text="💧", bg='#95a5a6', fg='white')
                else:
                    btn.configure(text="", bg='#34495e', fg='white')
    
    def player_shoot(self, row, col):
        """Handle player shooting at computer board"""
        if self.game_over or self.current_turn != 'player':
            return
            
        if (row, col) in self.player_shots:
            self.update_status("You've already shot there! Choose another target.")
            return
        
        self.player_shots.add((row, col))
        
        if (row, col) in self.computer_ships:
            self.computer_board[row][col] = 'X'
            self.update_status("🎯 Direct hit! Your turn continues.")
        else:
            self.computer_board[row][col] = 'O'
            self.update_status("💧 Miss! Computer's turn...")
            self.current_turn = 'computer'
            self.root.after(1000, self.computer_turn)
        
        self.update_board_display(self.computer_buttons, self.computer_board, hide_ships=True)
        self.check_winner()
    
    def computer_turn(self):
        """Handle computer's turn"""
        if self.game_over or self.current_turn != 'computer':
            return
            
        while True:
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
            
            if (row, col) not in self.computer_shots:
                self.computer_shots.add((row, col))
                break
        
        if (row, col) in self.player_ships:
            self.player_board[row][col] = 'X'
            self.update_status(f"💥 Computer hit your ship at ({row}, {col})! Computer continues.")
            self.root.after(1000, self.computer_turn)
        else:
            self.player_board[row][col] = 'O'
            self.update_status("Computer missed! Your turn.")
            self.current_turn = 'player'
        
        self.update_board_display(self.player_buttons, self.player_board, hide_ships=False)
        self.check_winner()
    
    def check_winner(self):
        """Check if there's a winner"""
        player_hits = sum(1 for ship in self.computer_ships if self.computer_board[ship[0]][ship[1]] == 'X')
        computer_hits = sum(1 for ship in self.player_ships if self.player_board[ship[0]][ship[1]] == 'X')
        
        if player_hits == len(self.computer_ships):
            self.end_game("Victory!", "🎉 Congratulations! You sank all enemy ships!")
        elif computer_hits == len(self.player_ships):
            self.end_game("Defeat!", "💔 The computer sank all your ships. Better luck next time!")
    
    def end_game(self, title, message):
        """End the game and show result"""
        self.game_over = True
        
        # Show all computer ships
        self.update_board_display(self.computer_buttons, self.computer_board, hide_ships=False)
        
        # Show result dialog
        result = messagebox.askyesno(title, f"{message}\n\nWould you like to play again?")
        if result:
            self.new_game()
        else:
            self.root.quit()
    
    def update_status(self, message):
        """Update the status message"""
        self.status_label.configure(text=message)
        self.root.update()
    
    def new_game(self):
        """Start a new game"""
        self.reset_game()
        
        # Place ships
        self.place_ships(self.player_board, self.player_ships)
        self.place_ships(self.computer_board, self.computer_ships)
        
        # Create boards
        self.player_buttons = self.create_board(self.player_frame_board, is_player_board=True)
        self.computer_buttons = self.create_board(self.computer_frame_board, is_player_board=False)
        
        # Update display
        self.update_board_display(self.player_buttons, self.player_board, hide_ships=False)
        self.update_board_display(self.computer_buttons, self.computer_board, hide_ships=True)
        
        self.update_status("🎯 Ready for battle! Click on enemy waters to fire!")
    
    def run(self):
        """Start the game loop"""
        self.root.mainloop()

def main():
    """Main function to run the game"""
    game = SankGameGUI()
    game.run()

if __name__ == "__main__":
    main()
