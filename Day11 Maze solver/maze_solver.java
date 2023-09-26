import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class MazeSolver {

    private static int[][] maze;
    private static int[][] solution;
    private static int numRows;
    private static int numCols;

    public static void main(String[] args) {
        if (args.length != 1) {
            System.out.println("Usage: java MazeSolver <maze_file>");
            return;
        }

        String mazeFile = args[0];

        if (readMazeFromFile(mazeFile)) {
            solution = new int[numRows][numCols];

            if (solveMaze(0, 0)) {
                System.out.println("Maze solution found:");
                printSolution();
            } else {
                System.out.println("No solution found.");
            }
        } else {
            System.out.println("Failed to read maze from file.");
        }
    }

    private static boolean readMazeFromFile(String fileName) {
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            int row = 0;
            int col = 0;

            while ((line = br.readLine()) != null) {
                if (row == 0) {
                    numCols = line.length();
                }
                numRows++;

                // Initialize the maze and solution arrays
                if (maze == null) {
                    maze = new int[numRows][numCols];
                }

                for (col = 0; col < numCols; col++) {
                    char cell = line.charAt(col);
                    if (cell == '0') {
                        maze[row][col] = 0; // Open path
                    } else if (cell == '1') {
                        maze[row][col] = 1; // Wall
                    } else {
                        System.out.println("Invalid character in maze file: " + cell);
                        return false;
                    }
                }

                row++;
            }

            return true;
        } catch (IOException e) {
            e.printStackTrace();
            return false;
        }
    }

    private static boolean solveMaze(int row, int col) {
        if (row == numRows - 1 && col == numCols - 1) {
            solution[row][col] = 1; // Mark the exit
            return true;
        }

        if (isValidMove(row, col)) {
            solution[row][col] = 1; // Mark the current cell as part of the path

            // Move down
            if (solveMaze(row + 1, col))
                return true;

            // Move right
            if (solveMaze(row, col + 1))
                return true;

            // If neither down nor right leads to the exit, backtrack
            solution[row][col] = 0;
        }

        return false;
    }

    private static boolean isValidMove(int row, int col) {
        return row >= 0 && col >= 0 && row < numRows && col < numCols && maze[row][col] == 0 && solution[row][col] == 0;
    }

    private static void printSolution() {
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                System.out.print(solution[i][j] + " ");
            }
            System.out.println();
        }
    }
}
