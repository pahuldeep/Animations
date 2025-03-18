from manim import *

class OnlineMachineLearning(Scene):
    def construct(self):
        # Create text labels
        title = Text("Online Machine Learning", font_size=36)
        title.to_edge(UP)

        # Create a box to represent the model
        model_box = Rectangle(width=3, height=2, color=BLUE, fill_opacity=0.5)
        model_label = Text("Model", font_size=24).move_to(model_box.get_center())

        # Create a box to represent incoming data
        data_box = Rectangle(width=3, height=2, color=GREEN, fill_opacity=0.5)
        data_label = Text("Incoming Data", font_size=24).move_to(data_box.get_center())

        # Create a box to represent the updated model
        updated_model_box = Rectangle(width=3, height=2, color=ORANGE, fill_opacity=0.5)
        updated_model_label = Text("Updated Model", font_size=24).move_to(updated_model_box.get_center())

        # Position the boxes
        data_box.next_to(title, LEFT, buff=0.5)
        model_box.next_to(data_box, DOWN, buff=0.5)
        updated_model_box.next_to(model_box, RIGHT, buff=0.5)

        # Align text labels
        data_label.move_to(data_box.get_center())
        model_label.move_to(model_box.get_center())
        updated_model_label.move_to(updated_model_box.get_center())

        # Add elements to the scene
        self.play(Write(title))
        self.play(Create(data_box), Write(data_label))
        self.play(Create(model_box), Write(model_label))

        # Simulate the online learning process
        for i in range(3):
            # Show incoming data
            self.play(Indicate(data_box))
            self.wait(1)

            # Update the model
            self.play(Transform(model_box, updated_model_box), Transform(model_label, updated_model_label))
            self.wait(1)

            # Reset the model for the next iteration
            self.play(Transform(updated_model_box, model_box), Transform(updated_model_label, model_label))

        # Final message
        final_message = Text("Model Updated with New Data!", font_size=24).to_edge(DOWN)
        self.play(Write(final_message))
        self.wait(2)

# To run the animation, use the following command in your terminal:
# manim -pql your_script_name.py OnlineMachineLearning
