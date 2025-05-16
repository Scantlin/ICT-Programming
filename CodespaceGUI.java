import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CodespaceGUI extends JFrame {

    public CodespaceGUI() {
        // Set up the main frame
        setTitle("GitHub Codespaces GUI Demo");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(400, 300);
        
        // Main panel with border layout
        JPanel mainPanel = new JPanel(new BorderLayout());
        mainPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        
        // Label at the top
        JLabel label = new JLabel("This is a GUI running in GitHub Codespaces");
        label.setHorizontalAlignment(SwingConstants.CENTER);
        mainPanel.add(label, BorderLayout.NORTH);
        
        // Text area in the center
        JTextArea textArea = new JTextArea();
        textArea.setEditable(false);
        textArea.setText("Since Codespaces doesn't have a display environment,\n" +
                         "this GUI isn't visible, but the code still runs.\n\n" +
                         "Check the console output for interaction results.");
        JScrollPane scrollPane = new JScrollPane(textArea);
        mainPanel.add(scrollPane, BorderLayout.CENTER);
        
        // Button panel at the bottom
        JPanel buttonPanel = new JPanel();
        JButton clickButton = new JButton("Click Me");
        JButton exitButton = new JButton("Exit");
        
        // Add action listeners
        clickButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                textArea.append("\nButton was clicked!");
                System.out.println("Button was clicked - this appears in the console");
            }
        });
        
        exitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.out.println("Exit button clicked - exiting program");
                System.exit(0);
            }
        });
        
        buttonPanel.add(clickButton);
        buttonPanel.add(exitButton);
        mainPanel.add(buttonPanel, BorderLayout.SOUTH);
        
        // Add main panel to frame
        add(mainPanel);
    }

    public static void main(String[] args) {
        // Check if we're running in a headless environment
        if (GraphicsEnvironment.isHeadless()) {
            System.out.println("Running in headless mode (no display available)");
            System.out.println("This program creates a GUI, but it can't be displayed in Codespaces.");
            
            // Simulate some GUI interactions
            System.out.println("\nSimulating GUI interactions:");
            System.out.println("1. Button click event occurred");
            System.out.println("2. Exit button clicked - exiting program");
            
            return;
        }
        
        // If we're not in headless mode, create and show the GUI
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                CodespaceGUI gui = new CodespaceGUI();
                gui.setVisible(true);
            }
        });
    }
}