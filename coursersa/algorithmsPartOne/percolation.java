public class Percolation {
    private int N;
    private WeightedQuickUnionUF grid;
    private WeightedQuickUnionUF gridB;
    private int[] openClosed;
    private int top;
    private int bottom;
   
    public Percolation(int N) {
        this.N = N;
        this.top = N*N;
        this.bottom = N*N+1;
        if (N <= 0) throw new IllegalArgumentException("N must be greater than 0");
        this.grid = new WeightedQuickUnionUF(N*N+2);
        this.gridB = new WeightedQuickUnionUF(N*N+2);
        openClosed = new int[N*N];
        
    }

    public void open(int i, int j) {
        int location = verifyLocation(i, j);
        openClosed[location] = 1;
        if (i == 1) {
            this.grid.union(top, location);
            this.gridB.union(top, location);
        }
        if (i == N) {
            this.grid.union(bottom, location);
            this.gridB.union(top, location);
        }
        int[] row = new int[4];
        int[] column = new int[4];
        row[0] = i - 1;
        row[1] = i + 1;
        row[2] = i;
        row[3] = i;
        column[0] = j;
        column[1] = j;
        column[2] = j + 1;
        column[3] = j - 1;
        int neighbor;
        
        for (int q = 0; q < row.length; q++) {
            try {
                neighbor = verifyLocation(row[q], column[q]);
            }
            catch (IndexOutOfBoundsException e) {
                neighbor = location;
            }
            if (neighbor != location)
                {
                    if (isOpen(row[q], column[q]))
                        {
                            this.grid.union(neighbor, location);
                            this.gridB.union(neighbor, location);
                        }
                }
            }    
        }  
    private int verifyLocation(int i, int j) {
        if (i > N || j > N || i <= 0 || j <= 0) 
            throw new IndexOutOfBoundsException("Coordinates entered are not in the grid");
        return (i-1) * this.N + (j-1);
    }
            
    public boolean isOpen(int i, int j) {
        int location = verifyLocation(i, j); 
        return openClosed[location] == 1;
    }

    public boolean isFull(int i, int j) {
        int location = verifyLocation(i, j);
        return this.grid.connected(location, top);
    }
    
    public boolean percolates() {
        return this.gridB.connected(top, bottom);
    }
}
