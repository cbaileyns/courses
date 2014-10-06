public class PercolationStats
{
    private int T;
    private int N;
    private double[] total;
    
    public PercolationStats(int N, int T) {
        this.T = T;
        this.N = N;
        if (N < 1 || T < 1) {
            throw new IllegalArgumentException();
        }
        this.total = new double[T];
        for (int q = 0; q < T; q++) {
            Percolation experiment = new Percolation(N);
            int count = 0;
            while (!experiment.percolates()) {
                int i = StdRandom.uniform(N) + 1;
                int j = StdRandom.uniform(N) + 1;
                if (!experiment.isOpen(i, j)) {
                    experiment.open(i, j);
                    count++;
                }
            }
           
            total[q] = (double) count / (this.N*this.N);
        }
    }
    public double mean() {
        return StdStats.mean(this.total);
    }
    public double stddev() {
        return StdStats.stddev(this.total);
    }
    public double confidenceLo() {
        return (mean() - (1.96*stddev()/Math.sqrt(this.T)));
    }
    public double confidenceHi() {
        return (mean() + (1.96*stddev()/Math.sqrt(this.T))); 
    }
    public static void main(String[] args) {
        int N = StdIn.readInt();
        int T = StdIn.readInt();
        PercolationStats ps = new PercolationStats(N, T);
        double mean   = ps.mean();
        double stddev = ps.stddev();
        double lower = mean - 1.96 * stddev / Math.sqrt(T);
        double upper = mean + 1.96 * stddev / Math.sqrt(T); 
        StdOut.println("mean                    = "+mean);
        StdOut.println("stddev                  = "+stddev);
        StdOut.println("95% confidence interval = "+lower+", "+upper);;
    }
}
            
