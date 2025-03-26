# Fretting-Fatigue-Failure-Simulation-with-Python-Scripting-in-Abaqus
Fretting fatigue failure is wear and fatigue damage at the interface of two surfaces under small cyclic motion, causing friction, wear debris, and crack formation. This project offers a guide on simulating Fretting Fatigue failure in Abaqus, focusing on 2D models, custom meshing, Field Outputs for analysis, and automating parameter selection with Python scripting.

The primary goal of this project is to create a 2D Fretting Fatigue model in Abaqus, focusing on model development, mesh optimization, and accurate contact stress analysis. A distinctive feature of this package is its emphasis on developing Python scripts to leverage the command prompt for automating post-processing. This tool enables the extraction of Field Outputs, generation of custom parameters from simulation data, and automation of key simulation modifications such as the Coefficient of Friction (CoF). Users will also learn how to run various simulation scenarios and collect output data from each run.

![Screenshot 2025-02-04 112858](https://github.com/user-attachments/assets/4b28c10c-c4e3-418c-861f-6acd3f809244)

In this repository, a portion of the Python script files are included. You can review them and get ideas for solving fretting fatigue failure problems.

For example, the stress extracted using this method in Abaqus for the fretting fatigue failure problem is shown in the figure below.

![Screenshot 2025-02-04 112355](https://github.com/user-attachments/assets/e16804ab-51e0-47cb-b249-36ece1fbb892)


Additionally, if you would like to access the full version of the codes and the Abaqus file, along with a 98-minute tutorial video that covers the fretting fatigue failure phenomenon, related equations and theory, how to implement it in Abaqus, and a step-by-step guide on writing Python scripts, we recommend checking out the complete package, the link to which is displayed on the right side of the repository.

![image](https://github.com/user-attachments/assets/ae6dbfa8-fb5e-49de-9dfc-ee9648a77e78)

It is worth noting that in some cases, the UEL subroutine is used to define custom elements in fretting and wear projects. With this in mind, if you're interested, you can check out our GitHub project on the UEL subroutine at the link below.

https://github.com/CAEAssistant-Group/Abaqus-UEL-Subroutine
