.. _introduction:

Introduction
------------

This introduction serves as the main entrypoint for just about anybody that wants to get to know the project.
And as you're already reading this document, *welcome*!

We're a small group of university students from Brno University of Technology, mainly Faculty of Electrical Engineering and Communication.
Our fascination in space & robotics has led us to building a competition Mars rover.

*What?!* There are Mars rover competitions? YES, multiple of them in fact.
Currently, we are aiming to attend the 2025 European Rover Challenge (ERC) competition taking place in Poland, but we won't stop there.

But why do we even do this? We believe that by cooperating on a complex tasks that require numerous expertises, we can all gain valuable experience that would be otherwise very hard to get at the university.
By working together with students of all relevant fields and study programmes, we form a unique team of ambitious students creating something we wouldn't be able to do individually.
But mostly, we just try to have fun.

Though virtually all of us are still students, we do have access to the labs & equiupment needed to support the core of our mission.
We also have enough hardware to build the first rover version provided by the robotics and artificial intelligence group from the department of control and instrumentation.
That said, we ultimately strive to be able to support our own operations by the means of institutional support and sponsorships.

Our rover is still in its infancy. It might look finished to the untrained eye, but the majority of the work is still to be done.
We do have a pretty good idea of how some of the things are going to be working in the *final* version though.

So here it is! Sorry for the ever accompanying lab mess, that's just how things are. This is the May 2024 state of things. 
We do have a first proof of concept rover able to move on its own. It can support its own weight together with all of the sensoric equipment, but nothing more.
As you can see, most of the build consists of aluminum extrusions, aluminum sheets and 3D printed parts - it kind of gets the job done quickly and cheaply! 

Inside, there are two battery packs that have enough juice for a few hours of driving around.
All of the wheels have integrated DC motors that can be driven independently.

On most of the competitions, the rover needs to be highly autonomous in executing its tasks.
For that, there *will* be multiple sensors allowing the rover to sense its surroundings and build a real-time map.
We employ lidars, cameras, IMUs, and other sensors to achieve this goal. Cooperating on such a project without an existing software framework would be a daunting task, so for that reason, we use ROS2 which has become a standart in robotic applications in the recent years.
To get everyone on the team up to speed, we offer periodic training for anyone interested. And before you ask, yes, we do use Linux on all of our devices.

Not interested in the autonomous navigation? There's more. The rover *will* also include a robotic manipulator able to move relatively heavy objects, but capable of precise movements at the same time.
We also have a prototype, but not yet attached to the rover as its being developed separately. 

Another big module, not yet ready to be mounted on the rover, will be the drilling instrument capable of drilling up to 30 cm deep into the martian soil and storing the sample afterwards.

.. toctree::
   :maxdepth: 2
   :caption: Introduction

   installation.md
   simulation.md
