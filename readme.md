# Final Project deploying a model remotely

The model can find the classification of pistachio by analyzing the model uploaded. The model has safeguards to avoid error generation. This is done by
introducing checkboxes. 
<br>
### **Both** checkbox must be checked before the upload button becomes available.

This was done to maximize the accuracy of the model.
- The image must have a square aspect ratio.
- The image must have a 24-bit color depth.
> The following conditions must be met to run the program.

### The program outputs two class names.
- Kirmizi
- Siirt

The model uses convolutional neural network, with sigmoid activation function to predict the pistachios species. It was trained on 1,717 pictures of pistachios.

The image used is licensed under CC0.

Note:

On small screens the sidebar may not be displayed immediately, kindly press the expand button to access more information.

Try the web app here -> https://jvbeldeniza-nut-detector-deployedmodel.streamlit.app/
