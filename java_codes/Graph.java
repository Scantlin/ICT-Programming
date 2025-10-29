import java.util.HashMap;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;

public class Graph {
    static class Graphs{
        private final Map<String, List<String>> adj = new HashMap<>();
    
        public void addVertex(String v){
            adj.computeIfAbsent(v, k -> new ArrayList<>());
        }

        public void addEdge(String u, String v){
            addVertex(u);
            addVertex(v);
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        public void printAdjacency(){
            for(var entry: adj.entrySet()){
                System.out.println(entry.getKey() + " -> " + entry.getValue());
            }
        }
}
    public static void main(String[] args) {
        Graphs g = new Graphs();

        g.addEdge("A", "B");
        g.addEdge("A", "C");
        g.addEdge("B", "D");
        g.addEdge("C", "D");

        System.out.println("Adjacency List:");
        g.printAdjacency();
    }
}
