---
title: PyData Barcelona (2017)
year: 2017
date: 2017-05-19
end_date: 2017-05-21
venue: ESADE
description: The Data Science conference from NumFOCUS
menu:
  main:
    parent: Other events
weight: 1
heroBackground: /images/photos/pydata_badges.jpg
layout: event
talks:
- id: opening-keynote
  title: Opening keynote
  speakers:
  - travis-oliphant
  type: keynote
  language: en
  description: 'Filmed at PyData Barcelona 2017


    www.pydata.org


    PyData is an educational program of NumFOCUS, a 501(c)3 non-profit organization in the United States. PyData provides a forum for the international community of users and developers of data analysis tools to share ideas and learn from each other. The global PyData network promotes discussion of best practices, new approaches, and emerging technologies for data management, processing, analytics, and visualization. PyData communities approach data science using many languages, including (but not limited to) Python, Julia, and R.


    PyData conferences aim to be accessible and community-driven, with novice to advanced level presentations. PyData tutorials and talks bring attendees the latest project features along with cutting-edge use cases.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=NBliyFXnWeo
  title_note: 'pyvideo stored the role line of the speaker where the title goes, "Chief Data Scientist and co-founder of Continuum Analytics", and no source names the talk. "Opening keynote" is what it was.'
- id: the-magic-behind-pyspark-how-it-impacts-perf-the-future
  title: The Magic Behind PySpark, how it impacts perf & the "future"
  speakers:
  - holden-karau
  type: keynote
  language: en
  description: 'A look at how PySpark "works" today and how we can make it better in the future + insert engine noises of a fast car +


    **Abstract**


    This talk will introduce PySpark along with the magic done to make it work and be friends with the JVM. We will discuss why lazy evaluation makes a huge difference in PySpark, both in terms of general optimizations it opens up as well as Python specific considerations. From there we will explore much of the future of Spark, DataFrames & Datasets and what this means for PySpark. Most Spark DataFrame examples limit them selves to things written in the relational style query language, but we will explore how to add more functionality through UDFS.


    We will wrap up with looking at the different pieces of work being done to make PySpark faster, from using better interchange formats like Apache Arrow to crazy hair brained schemes inspired by (but not the fault of) the Javascript on Spark project.


    Hopefully no one is scared away from using Spark once they see the 300 small gnome like creatures behind the curtain, but parental guidance is encouraged for those who still believe in magic, reliable distributed systems, and vendor marketing brochures.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=TI05I_8uS3U
- id: a-beginners-guide-to-weather-climate-data
  title: A Beginners Guide to Weather & Climate Data
  speakers:
  - margriet-groenendijk
  type: talk
  language: en
  description: 'Weather is part of our every day lives. Who doesn''t check the weather forecast regularly? But where does the data come from, what is it made of? The answer is a mix of measurements and models. This session looks at observations, predictions and forecast models, and weather data as a variable to consider in machine learning models. Learn how it is done from several Python notebook examples.


    **Abstract**


    Weather is part of our every day lives. Who doesn''t check the rain radar before heading out, or the weather forecast when planning a weekend away? But where does this data come from, what is it made of, and what can you do with it? The answer is a mix of measurements, models and statistics. This session will use Python notebooks with examples of how it is done:


    * Weather is quantified by the temperature, humidity, wind, rainfall and radiation. These variables are all measured at thousands of locations worldwide and all data is collected and checked to improve the weather forecasts. Learn how to interpolate this data to create for instance global temperature maps to estimate the global monthly and annual temperature.

    * The observations are used to constrain the global weather forecast models. These models are complex and simulate the energy, water and carbon fluxes between and in the atmosphere, ocean and land. The output from the models is gridded data, which is generally stored in binary netcdf files. Learn how to load and process the gridded data into time series or maps for further analysis.

    * The raw model data is processed for you when you request weather data through a REST API. Learn how to use a weather API to train a supervised model with historical weather time series and then use the weather forecast data to do predictions. This session provides you with a brief overview of the science behind weather and climate forecasts and gives you the tools to get started with weather data.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=U_Aq2cPxwss
  - type: slides
    url: https://www.slideshare.net/MargrietGroenendijk/pydata-barcelona-weather-and-climate-data
- id: despicable-machines-how-computers-can-be-assholes
  title: 'Despicable machines: how computers can be assholes'
  speakers:
  - maciej-siwek
  type: talk
  language: en
  description: 'There''s a widespread belief among machine learning practitioners that algorithms are objective and allow us to deal with the messy reality in a nice, objective way, without worrying about all the yucky human nature things. This talk will argue that this belief is wrong. Algorithms, just like the humans who create them, can be severely biased and despicable indeed.


    **Abstract**


    When working on a new ML solution to solve a given problem, do you think that you are simply using objective reality to infer a set of unbiased rules that will allow you to predict the future? Do you think that worrying about the morality of your work is something other people should do? If so, this talk is for you.


    In this brief time, I will try to convince you that you hold great power over how the future world will look like and that you should incorporate thinking about morality into the set of ML tools you use every day. We will take a short journey through several problems, which surfaced over the last few years, as ML and AI generally, became more widely used. We will look at bias present in training data, at some real-world consequences of not considering it (including one or two hair-raising stories) and cutting-edge research on how to counteract this.


    The outline of the talk is:


    * Intro the problem: ML algos can be biased!

    * Two concrete examples.

    * What''s been done so far (i.e. techniques from recently-published papers).

    * What to do next: unanswered questions.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=8kL71zk4KNk
- id: how-to-manage-complexity-in-distributed-applications
  title: How to manage complexity in distributed applications
  speakers:
  - guillem-borrell-nogueras
  type: talk
  language: en
  description: 'Complexity is tricky. Some years ago we got how to scale the performance of distributed applications, and that''s why everyone is talking about Big Data. But the challenge now is scaling the complexity within a fast-changing environment without penalizing the performance. These are the conclusions after one year developing a library trying to handle this issue, and using it in production.


    **Abstract**


    The development of large-scale distributed applications is an engineering challenge by itself. Development has to be orthogonal to be scalable, as you may know if you have heard about the Mythical Man-Month and the Conway''s law: trying to make your application faster may slow down your development. Managing complexity is a new technology trend, and NFQ and the Carlos III University of Madrid have developed a library to make large-scale distributed applications more sensible called pylm (https://pylm.readthedocs.io). Since this library has been already used in production, it is time to summarize what are the challenges one faces when building something more intricate than a Spark cluster.


    This talk is about the value of developing in-house tools and obtaining deep technological insight opposed to the successive integration of trendy technologies. The latter is suitable to implement one-shot tools for isolated projects, but when facing a multi-year complex project, the former becomes a more solid ground for long-term maintenance. Complexity piles up nonlinearly, and the most popular tools nowadays cringe when they have to be tightly integrated, since in the long term it is impossible to isolate the technical and the human aspects of development.


    Complexity''s weight is getting heavier in this scalability-obsessed world, and it''s time to talk about it.


    This project has been funded by the Spanish Ministry of Economy and Competitivity under the grant IDI-20150936, cofinanced with FEDER funds'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=rPDZg2--5uM
- id: feature-importance-and-ensemble-methods-a-new-perspective
  title: 'Feature Importance and Ensemble Methods : a new perspective'
  speakers:
  - constant-bridon
  type: talk
  language: en
  description: 'Ensemble methods are extremely performant in terms of prediction, but lack easy interpretation. Feature importance is not only counting up how many times a feature has been used in a weak learner, but also by how much this feature contributes to the result. Detailed example and implementation are provided in a jupyter notebook in python for the library "xgboost" of extreme gradient boosting.


    **Abstract**


    I - Feature importance in ensemble algorithms - state of the art


    1) Feature importance in sklearn/xgboost: basically counts the occurrences of a feature in all the weak learners

    2) Construction of the trees in xgboost: if the trees are deep enough, every feature is going to be used

    3) Global feature importance is a misleading: a given feature might be critical for a given subpopulation but completely irrelevant for another (ex : multi-class classification)


    II - Xgboost real feature importance


    1) Prediction influence: first splits influence the prediction more than last splits, so the importance of a feature must be weighted by the discrimination it provides


    2) Point-to-point feature importance: following the path of a given prediction, it is possible to weigh the importance of every used feature


    3) A relevant assessment of feature importance: explanation of a given prediction, and aggregation on a set of data points


    III - Implementation and examples


    1) Point-to-point feature importance illustration and implementation explanation


    2) Evolution of feature importance with respect to learning iterations


    3) Noisy variables cancellation


    IV - Limits and ways forward


    1) A word on correlated variables


    2) Is there a compromise performance/interpretation ?'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=qdEhJ0uT7wk
- id: happiness-inside-a-job-a-social-network-analysis
  title: 'Happiness inside a job: a social network analysis'
  speakers:
  - guillem-duran-ballester
  type: talk
  language: en
  description: 'In this talk, we will show how to analyze social network data from a mobile phone application to predict employee turnover and employee happiness. We will look into the process of extracting new features from a dataset using social network analysis techniques. We will also show how these features can be visualized and used to boost machine learning models.


    **Abstract**


    In this talk, we will show how to analyze social network data to predict employee turnover and employee happiness. This talk is a summary of different notebooks about social network analysis that will be available on [Github](https://github.com/Guillem-db/PyData-Bcn-2017). Please note that all the methodology and details we are using, are explained in depth in the notebooks.


    We will cover the following topics:


    * From tables to graphs: How to use [pandas](https://pandas.pydata.org/) and [networkx](https://networkx.github.io/) to merge several DataFrames into a graph, and different criteria for creating a graph representation of a database.


    * Graph features: How to extract new features using social network analysis techniques such as [`Non-Negative Matrix Factorization`](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.NMF.html) and graph [`centrality metrics`](https://networkx.github.io/documentation/development/reference/algorithms.centrality.html). We will explain what these features represent, and how they relate to other types of features that can be extracted directly from the database.


    * Improving ML models: How to use graph features to boost machine learning models. We will talk about different feature selection techniques that can be used to filter out the most significant set of graph-based features using [scikit-learn](https://scikit-learn.org/).


    * Visualization: How to visualize social interactions using [bokeh](https://bokeh.pydata.org/en/latest/), and how visualization techniques can be used to check data integrity.


    We will also review common mistakes that can happen during the modeling process and, how to prevent invalid data from getting leaked into your machine learning models. To conclude we compare the merits of using a Python framework versus R Language in terms of development time and computational performance. Data set provided by https://myhappyforce.com'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=2Ot3gyGLVA0
  - type: slides
    url: https://github.com/Guillem-db/Happiness-inside-a-job-PyDataBcn17
- id: machine-learning-to-know-if-you-r-coming
  title: Machine Learning to know if you R coming
  speakers:
  - claudia-guirao
  type: talk
  language: en
  description: 'Predicting Hotel Reservation Cancellations with R language.


    Knowing in advance bookings that will be canceled before the arrival date is crucial in the hotel sector. We will examine the determinant characteristics of reservation cancellation, the constrains of this project and how the probability of cancellation was estimated.


    **Abstract**


    Some users are more likely to cancel their bookings than others, depending on several factors/conditions. Knowing these factors and how many bookings will be canceled will help hotels to optimize their incomes and maximize their occupancy.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=IlofEE7Sswc
- id: analyzing-code-contributions-to-the-cpython-project-using
  title: Analyzing code contributions to the CPython project using NetworkX and Matplotlib
  speakers:
  - jordi-torrents
  type: talk
  language: en
  description: 'It''s a well established fact that only a small fraction of developers account for most code contributions to FOSS projects. The CPython project is not an exception, but analyzing code contributions through time reveals that the people that contribute the most is not always the same. I model CPython''s contribution dynamics as cooperation networks and analyze them using NetworkX and Matplotlib.


    **Abstract**


    I analyze cooperation on the CPython project by analyzing the code contributions that each participant on the project has done through time. I model these contributions as a succession of bipartite networks where the bipartite node sets are contributors and source code files; each contributor is linked to the source files to which they have contributed, weighted by the number of lines of source code added. Analyzing the structure of these networks using NetworkX and Matplotlib I found an hierarchy of nested groups of developers that corresponds to the developers that do most of the code contributions in the CPython project. This hierarchy, on the one hand, reflects the empirically well established fact that in FOSS projects only a small fraction of the developers account for most of the contributions. And, on the other hand, refutes the naive views of early academic accounts that characterized FOSS projects as a flat hierarchy of peers in which every individual does more or less the same. I argue that the structure of CPython''s cooperation network can be characterized as an open elite, where the top levels of this hierarchy are filled with new individuals at a high pace. This feature is key for understanding the mechanisms and dynamics that make FOSS communities able to develop long term projects, with high individual turnover, and yet achieve high impact and coherent results as a result of large scale cooperation.


    You can download the slides for this talk from https://github.com/jtorrents/thesis/blob/master/presentations/pydata_bcn/cpython_code_contributions.pdf'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=4YqMpYqjqps
  - type: slides
    url: https://github.com/jtorrents/thesis/blob/master/presentations/pydata_bcn/cpython_code_contributions.pdf
- id: running-jupyter-notebook-remotely-in-a-docker-swarm-cluster
  title: Running jupyter notebook remotely in a docker swarm cluster
  speakers:
  - jordi-deu-pons
  type: talk
  language: en
  description: 'The current version of Jupyter Notebook computes the document state at the browser side, this is a problem if you run long jobs in a remote notebook from a laptop. If you close the browser you lose all the output of the current running cell. I will explain how we solved this problem in our lab. This solution it also allows a "walkie-talkie" like real-time collaboration.


    **Abstract**


    The solution is based on running a docker container with a browser and a VNC server. All the remote access to the notebooks is done using Apache Guacamole a clientless remote desktop gateway. Everything is running on a dynamic docker swarm cluster of 20 nodes. As a lateral effect, this solution it also allows a real-time collaboration between users in a way that multiple users can access at the same time the same desktop (but they have to fight for the mouse and the keyboard).


    https://github.com/jordeu/pytalks/tree/master/20170520_pydata_jupyter_in_a_docker_cluster'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=0XYRr6MLrVA
- id: tensorflow-wide-deep-advanced-classification-the-easy-way
  title: 'TensorFlow Wide & Deep: Advanced Classification the easy way'
  speakers:
  - yufeng-guo
  type: talk
  language: en
  description: 'In this talk, we will go on an adventure to build a machine learning model that combines the benefits of linear regression models with deep neural networks. You will also gain some intuition about what is happening under the hood, and learn how you can use this model for your own datasets.


    **Abstract**


    Deep learning has already revolutionized machine learning research, but it remains out of reach for many developers. However, tools already exist today that enable leading-edge machine learning for many problem domains.

    In this talk, we will go on an adventure to build a machine learning model that combines the benefits of linear models with deep neural networks. You will also gain some intuition about what is happening under the hood, and learn how to use this model for your own datasets! To accomplish this, we will use TensorFlow, an open-source machine learning library with a full Python interface. It has become the most popular machine learning library on GitHub, and the community around it is growing rapidly.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=WKgNNC0VLhM
  - type: slides
    url: https://storage.googleapis.com/yufengg-slides/pydataBCNslides.pdf
- id: deepcare-chatbot-generating-answers-to-customers-using-deep
  title: DeepCare Chatbot - Generating answers to customers using Deep Learning and NLP
  speakers:
  - pascal-van-kooten
  type: talk
  language: en
  description: 'The DeepCare chatbot is capable of learning to answer customer questions. Using a hybrid approach of NLP and Deep Learning, it tries to combat logical fallacies that occur in pure deep learning bots, while still coming up with unique answers.


    In particular, it uses a sequence-to-sequence (seq2seq) long-short-term-memory LSTM deep learning model to capture intricacies in questions. As organisations cannot afford a bot making logical mistakes, verification through NLP is used. This two-step model prevents the downside of "no control" on deep learning, as well as the too static nature of classical rule based NLP models, and thus enables potentially higher quality answers.


    A live demo will be available at https://deepcare.online on the day of the talk.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=PF0HCAmzz7U
  - type: slides
    url: https://www.slideshare.net/PascalvanKooten/deepcare-chatbot-generating-answers-to-customers-using-a-hybrid-approach-of-deep-learning-and-nlp
  title_note: 'The Slides list of the pre-Hugo page named it "DeepCare Chatbot - Generating answers to customers using a hybrid approach of Deep Learning and NLP", the title of the slides. The video names it as above.'
- id: extending-jupyter-with-google-cloud-storage-file-system
  title: Extending Jupyter with Google Cloud Storage file system backend
  speakers:
  - egor-bulychev
  type: talk
  language: en
  description: 'Jupyter has a modular architecture which allows extending it in numerous ways. This talk presents src-d/jgscm, Google Cloud Storage Jupyter file system backend which provides the ability to work with notebooks and other files directly in Google Cloud Storage. The described approach can be used for writing similar backends, e.g. for Amazon Cloud.


    See more here : https://egorbu.github.io/pydata_2017_barcelona/index.html


    **Abstract**


    src-d/jgscm is a Jupyter file system backend for Google Cloud Storage. It allows to work with notebooks and other files directly in Google Cloud Storage. It''s codebase is rather small and simple thanks to Jupyter''s modular architecture. We start from the very basics, revise how Google Cloud Storage works and how Jupyter deals with the virtual file system and end up with the complete production-tested backend implementation. The described ideas are rather versatile and can be re-used to create backends for similar cloud storage systems, e.g. Amazon.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=uLC0t5JZBZs
- id: the-secret-life-of-rolling-pandas
  title: The Secret Life Of Rolling Pandas
  speakers:
  - jaime-fernandez-del-rio
  type: talk
  language: en
  description: 'Pandas provides a powerful set of functions to compute statistics on rolling windows. We will go beyond the convenient interface, and peek at the algorithmic gems that implement these operations efficiently: summed area tables, Welford''s method, skip lists, ring buffers, deques... will all get their minute of fame, and attendees may learn a thing or two they can use in their everyday coding.


    **Abstract**


    The talk will cover:


    * A quick overview of the Rolling and Expanding objects in pandas. Why straightforward implementations, even clever ones using advanced NumPy tricks, are inefficient.

    * How is Series.rolling().sum() implemented. How the same idea can be extended to higher dimensions with the help of the inclusion-exclusion principle to yield summed area tables.

    * How are Series.rolling().var() and friends implemented. The importance of numerically stable algorithms: why Welford''s method is the better choice, even if it''s a little slower. How can the same ideas be generalized to higher order moments, and used to parallelize computations.

    * How are Series.rolling().max() and .min() implemented. The beauty of clever algorithms. The use of specialized data structures: a ring buffer as a deque.

    * How are Series.rolling().median() and .quantile() implemented. More specialized data structures: the skip list, or why randomization can be your friend.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=XM_r5La-1tA
- id: nasa-space-apps-challenge-asteroid-prediction-impact
  title: 'NASA Space APPS Challenge: Asteroid prediction impact'
  speakers:
  - gema-parreno
  type: keynote
  language: en
  description: 'TensorFlow and Prophet : Forecasting Asteroid impact with opensource software Talk about NASA Space APPS 2016 global finalist project , focused on neural net design


    **Abstract**


    The talk will have two separate parts ; the first of it focuses on explaining Tensorflow architecture and Prophet opensource tools and the second part will dive into the Neural Net design and forecast prediction .'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=8h3uyQfiMNc
- id: squeeze-gently-your-data
  title: Squeeze (gently) your data
  speakers:
  - francesc-alted
  type: keynote
  language: en
  description: 'Coping with the growing rate of data sources is becoming a big challenge, not only in terms of efficiently storing it, but also (and most specially) in doing more general computations with them. Compressing your data may help in many (and sometimes unexpected) ways in this task. This talk will introduce several ways in which you can benefit from highly efficient compression libraries.


    **Abstract**


    Nowadays CPUs are fast; they are coming with more and more cores and, in comparison, memory speed is not keeping this race in terms of speed. As a result, this opening gap is what is making of compression a valuable technique, not only for storing the same data by using less storage but also to accelerate data handling operations in an increasing number of cases.


    My talk will start by introducing the technological reasons behind the increasing benefit of using compression in data science, and then will show some practical cases where data compression can lead to much more efficient data pipelines. For this, I will be using well-proven compression libraries like [Blosc](https://www.blosc.org/), [Zstandard](https://github.com/facebook/zstd) and [LZ4](https://github.com/lz4/lz4) that, either in combination with data handling libraries (like [PyTables](https://www.pytables.org/), [bcolz](https://bcolz.blosc.org/en/latest/) or [zarr](https://zarr.readthedocs.io/en/latest/)), or used for handling high-speed data streams (transmitted e.g. via [gRPC](https://www.grpc.io/)).'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=o9PC4JC74tU
  - type: slides
    url: https://speakerdeck.com/francescalted/squeeze-gently-your-big-data
- id: increasing-the-trading-prediction-by-mining-aggregated
  title: Increasing the trading prediction by mining aggregated human texting messages
  speakers:
  - yang-liu
  type: talk
  language: en
  description: 'A novel approach is proposed to predict intraday directional-movements of the stock in the trading market based on the text of breaking financial news or social media by event data. This work is an effort to put more emphasis on the text-mining methods and tackle some specific aspects thereof that are weak in previous works. The research is a specific market, namely, the trading and stock market,


    **Abstract**


    Sentiment analysis This step is observed the time series of the company''s event based on the financial news or the social media, which analyses problem of coreference in text mining that is sentiment classification. Fasttext is inspired method that focuses on the meaning of words, which solves to obscure by ambiguity and play on words. This way can classify polarity, subjectivity and intensity in the corpus. According to the results of the classification, then it changes to the word representation. Thus, prediction accuracy increases significantly at this layer that is attributed to appropriate noise-reduction from the feature-space. Model creation and prediction The first layer is termed Sentiment Integration Layer by the deep neural network, which integrates sentiment analysis capability into the algorithm by proposing a sentiment weight that reflects their sentiment. Additionally, this layer reduces the dimensions by eliminating value in terms of sentiment and thereby improves prediction accuracy. The second layer encompasses a deep neural network model creation algorithm. It updates the models with the most recent information available, the deep learning algorithm is extensively evaluated using real market data and news content across multiple years, which is a good fitting capability to evaluate and select the financial news. The third layer is that it uses the recursive neural network explore patterns and of financial news through the recursive and pooling operation.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=G2GuL-xPhJA
  - type: slides
    url: https://drive.google.com/open?id=0B19Xo1zu3JtgZmVDaWVyTk1uN3M
- id: the-neuroscience-lab
  title: The Neuroscience Lab
  speakers:
  - nicholas-a-del-grosso
  - javier-martinez-alcantara
  type: talk
  language: en
  description: 'Python is an excellent fit for scientists; it is readable, has an active scientific community, and, most importantly, is versatile across a wide variety of programming tasks. In this talk, we will celebrate this versatility of Python by sharing the research being done in our neuroscience laboratory, focusing on Python''s involvement in each step of our scientific research.


    **Abstract**


    Biologists have always built their own hardware to perform unique experiments; today, new data collection and analysis techniques demand that they develop their own software as well. Often, this means that researchers without a formal education in programming must perform a wide variety of programming tasks in order to perform cutting-edge research. As a "real" programming language, Python is an excellent fit for scientists, not only for its oft-celebrated readability, active scientific community, and cross-platform support, but also for its versatility across a wide variety of domains. In this talk, we will celebrate this versatility of Python by sharing the research being done in our neuroscience laboratory, focusing how Python packages, applications, and plugins have become the tools of choice for everything from real-time machine vision and 3D graphics to data analysis and the presentation of scientific results.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=pdrX1qdjvxE
  - type: slides
    url: https://www.slideshare.net/JavierMartinezAlcant/neuroscience-lab-a-tour-through-the-eyes-of-a-pythonista-pydata-barcelona2017
  title_note: 'The Slides list of the pre-Hugo page named it "Neuroscience Lab, a tour through the eyes of a pythonista", the title of the slides, and credited Javier Martínez Alcántara alone. The video names it as above and credits both speakers.'
- id: web-scraping-with-python
  title: Web Scraping with Python
  speakers:
  - carles-illa
  type: talk
  language: en
  description: 'Web Scraping is widely used to get data from websites automatically. Whether it be contact information, news or selling prices, we rely on web scraping techniques as they allow us to collect large data with minimal effort.


    In the Python ecosystem we have a lot of different tools for extracting data from web pages, and in this talk we will present some of the most powerful ones.


    **Abstract**


    Web Scraping is the process of extracting useful information from the web automatically.


    It is widely used for various purposes like:


    - Lead generation

    - Price monitoring on e-commerce sites

    - Product reviews collection to do sentimental analysis

    - Social profiles retrieving for recruiters

    - Scraping blogs & forums to keep up with trends and news

    - Maintaining up-to-date real estate databases

    - News aggregators

    - Reputation monitoring

    - Events listings

    - Websites changes detection

    - Etc.


    In this talk we will present some of the most powerful tools for extracting data from web pages using Python. We will learn how to use Python to request information from a web server, how to perform basic handling of the server''s response, and how to begin interacting with a website in an automated fashion.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=aTwvQZjEZhk
- id: guillotina-an-async-rest-resource-db-to-manage-millions-of
  title: Guillotina - An Async REST Resource DB to manage millions of objects
  speakers:
  - ramon-navarro-bosch
  type: talk
  language: en
  description: 'Guillotina is a new framework designed to be horizontal scalable, build on top of aiohttp and offering a Resource REST API to store, read and query object oriented datasets with millions of elements. Based on JSON schema types allows to define a Traversal API with strong security and granularity. With an abstracted storage layer its possible to provide support for Couch, Cassandra and Postgres.


    **Abstract**


    One of the most common problems on my daily basis data management is a way to store and secure objects with information in a transactional scalable infrastructure. Having an async API that holds security, triggers and transactional operations allows to provide an interface for managing the data that will be processed by the machine learning engines on batch operations. Including async queues of operations allows to provide model inference on the objects on real time operations on objects on the stack.


    After 15 years on Plone/Zope framework we started to design a new concept using all the lessons learned on content management to provide a CRUD storage layer for big data objects.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=IkIfxkI5qpY
  - type: slides
    url: https://www.slideshare.net/bloodbare/guillotina-76266421
- id: lymphos2-organizing-and-sharing-biological-data
  title: LympHOS2, Organizing and Sharing Biological Data
  speakers:
  - oscar-gallardo-roman
  type: talk
  language: en
  description: "The study of the proteome (the set of proteins expressed by a cell,\ntissue, or organism at a defined time and conditions) generates a large\namount of complex data. This data should be processed, stored, curated,\nand made easily available to researchers so it can be studied to obtain\nbiomedical knowledge. In this talk we expose the Python tools we have\nused and developed to accomplish it.\n\nAbstract\n\nAt the [LP-CSIC/UAB](https://proteomica.uab.cat) we use a technology called [Mass Spectrometry](https://en.wikipedia.org/wiki/Mass_spectrometry) to\nstudy the *phospho-proteome of human T-Lymphocytes*; this is, the group\nof proteins that are phosphorilated (modified with phosphate groups) in\nthe human [T cells](https://en.wikipedia.org/wiki/T_cell) during their activation and differentiation as part\nof the [immune response](https://en.wikipedia.org/wiki/Immune_response). The experiments involved in this study\ngenerates a *large* amount of *complex* data:\n\n- Experimental conditions and procedures metadata.\n- The spectra data and metadata obtained from the mass spectrometers\n (usually in proprietary binary formats).\n- Qualitative or identification data, consisting of search results of\n those spectra against human protein sequence databases (using\n multiple search engines, that use different output file-formats)\n linking the spectra with possible peptides (small protein sequence\n fragments) that may or may not contain phosphorylated amino-acids.\n- Semi-quantitative data about the abundance of each possible\n identified peptide.\n- Missing values, identification scores, phosphorylation reassignments,\n and a lot of relationships and inter-linked data...\n\nAnd all this data has to be **processed**, **stored**, **curated**, and\nmade **easily accessible** to researchers in our lab and worldwide, so\nthey can study it to obtain biomedical knowledge about the\nphosphorylation changes in peptides and proteins involved in the signal\ntransduction pathways of T cells after their activation during the\nspecific immune response.\n\nWe have used different Python *packages* to develop different tools and\napplications to accomplish those objectives:\n\n- The [EasierMgf](https://bitbucket.org/lp-csic-uab/easiermgf) front-end application, to extract plain text spectra\n data from proprietary binary mass spectrometer files, was developed\n using the [wxPython](https://wxpython.org/) GUI toolkit.\n- The [ORM](https://en.wikipedia.org/wiki/Object-relational_mapping) from the [django](https://www.djangoproject.com/) framework was used to design and\n interact with the LymPHOS2 [MySQL](https://www.mysql.com/) database, which stores all the\n data and their inter-relationships.\n- Also, different modules from the Python standard library (*json*,\n *xml.etree.ElementTree*, *csv*, *zipfile*) were used to read and\n [import](https://bitbucket.org/lp-csic-uab/lymphosweb/src/c127cd7a88a5dfb0a70b9e3b6243553c6adda6fb/src/LymPHOS_v1_5/lymphos/filters.py) into the database the different files containing the data;\n and to [export](https://bitbucket.org/lp-csic-uab/lymphostools) database data into commonly used file formats for\n the researches to work with.\n- The [PQuantifier](https://bitbucket.org/lp-csic-uab/lymphospquantifier) group of tools was developed to do the statistical\n processing and analysis of the LymPHOS2 semi-quantitative data. It\n uses the [SQLAlchemy](https://www.sqlalchemy.org/) ORM for fast database storage in local\n [SQLite](https://sqlite.org/) files, the [NumPy](https://www.numpy.org/) N-dimensional array package, the\n [SciPy](https://scipy.org/scipylib) scientific computing library for the statistics, the\n [uncertainties](https://pythonhosted.org/uncertainties/) package for calculations with error propagation,\n and the [matplotlib](https://matplotlib.org/) 2D plotting library for some nice plots of\n data distributions.\n- And the full django framework itself was used to develop the\n [LymPHOS2](https://www.lymphos.org) web application. Which also uses the matplotlib library\n to dynamically generate the mass spectra images.\n\nThe final result is the `LymPHOS2 <https://bitbucket.org/lp-csic-uab/lymphosweb/branch/Web_LymPHOS_2>`_ web-oriented database, that\nnowadays (2017) contains 131.908 mass spectra, 15.566 phosphorylation\nsites from 8.273 unique phospho-peptides and 4.937 proteins (which\nrepresent a 45-fold increase over the original LymPHOS database of\n2009); aside from the new quantitative data for 1.975 of the identified\nphospho-peptides, which was not present in the previous version of\nLymPHOS.\n\n**Repositories and Presentation Slides:**\n\n- Bitbucket code repositories: https://bitbucket.org/lp-csic-uab/\n- Presentation Slides (.ODP, .PDF and .PPTX):\n https://bitbucket.org/lp-csic-uab/lymphosdocs/downloads/\n\n**Credits:**\n\nThe exposed work has been carried out at [LP-CSIC/UAB](https://proteomica.uab.cat) from\n[Catalonia](https://en.wikipedia.org/wiki/Catalonia), part of the `Spanish National Research Council (Consejo\nSuperior de Investigaciones Científicas - CSIC)`_ and of `ProteoRed\n(Proteomics National NetWork Platform)`_.\n\nThe *people* who have participated directly in the current work are:\n\n- **Data analysis, bioinformatics and informatics**: *Joaquin Abian*\n and *Óscar Gallardo*.\n- **Mass Spectrometry, experimental design and implementation**:\n *Montserrat Carrascal*, *Nguyen Tien Dung* and *Oriol Vidal-Cortes*.\n- **Sample preparation**: *Montserrat Carrascal*, *Nguyen Tien Dung*,\n *Oriol Vidal-Cortes* and *Vanessa Casas*.\n- **Past collaborators**: *David Ovelleiro* and *Marina Gay*.\n- **Direction**: *Joaquin Abian*."
  links:
  - type: video
    url: https://www.youtube.com/watch?v=IpZeg2siLVU
  - type: slides
    url: https://bitbucket.org/lp-csic-uab/lymphosdocs/downloads/
  title_note: 'The Slides list of the pre-Hugo page named it "LympHOS2, Organizing and Sharing Biological Data of the Human Lymphocyte Proteome using Python". The video names it as above.'
- id: prototyping-interactive-dashboards-with-jupyter-notebooks
  title: Prototyping Interactive Dashboards with Jupyter Notebooks
  speakers:
  - camilo-cardona
  type: talk
  language: en
  description: 'In this talk, I describe my experience in using jupyter-dashboards, ipywidgets and other libraries to build basic prototypes of data exploration dashboards for datasets related to Internet traffic and packet-switching networks. We''ll go over various examples on how to build and use the widgets to navigate the data, visualize analysis, and evaluate optimization changes.


    **Abstract**


    As python programmers, we often use jupyter notebooks as a platform for reproducible data analysis and publication of results. The jupyter ecosystem is still under-utilized for projects that require interactions from non-coder users, such as explorative dashboards or Business intelligence applications. There are other specialised options for these UI/UX interfaces, but integrating them into the analysis pipeline (e.g. Jupyter) is often rather hard. Preferably, we would be able to prototype these interactive applications without leaving our environment.


    Jupyter-dashboards, ipywidgets, and other typical pydata libraries provide jupyter with the capabilities to create flexible, and rather powerful interactive elements. This toolset can be used in small projects to create the final facing interface for a limited number of end users. For bigger projects, a more robust UI/UX is normally required to support larger number of simultaneous users. However, the jupyter-dashboard/ipywidgets toolset can still be useful in these cases as an end-to-end prototyping platform, allowing us to get feedback from users at early stages of the project, thus helping us better steer our development.


    In this talk, I share experiences of using this toolset for different use cases related to analysis of Internet traffic and network engineering. I''ll go over examples of how to build widgets to explore the Internet traffic and other network data, while highlighting some of its characteristics. Furthermore, I''ll describe some optimisations performed by network engineers on their traffic, such as load balancing, and how the tools can be used to evaluate them.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=LAy8vD4PQLg
  - type: slides
    url: https://github.com/jccardonar/pydata_bcn_presentation
  title_note: 'The Slides list of the pre-Hugo page named it "Prototyping Interactive Dashboards with Jupyter Notebooks: Examples from Network Engineering". The video names it as above.'
- id: blockchain-and-smart-contracts-explained-and-simplified
  title: Blockchain and smart contracts explained (and simplified)
  speakers:
  - guillem-borrell-nogueras
  type: talk
  language: en
  description: 'Blockchain is the next big thing that will revolutionize everything, but no one knows how. The same can be said about smart contracts. Bitcoin and Ethereum are great technologies, but too complex for most cases. This talk will explain why smart contracts are hard, and why they don''t need to be. Finally, a simple ledger for smart contracts in python (pyledger) will be presented.


    **Abstract**


    Smart contracts are an old and simple concept. They are just computer programs that facilitate the negotiation and settlement of contracts by several parties. Their goal is to lower the transaction latency and cost associated with human middlemen. The blockchain technology brought the possibility to sanction contracts when peers do not trust each other, which is necessary for applications like virtual currencies. However, due to the CAP theorem and the cost of the Byzantine consensus, their performance tends to be quite bad.


    Current smart contract platforms such as Ethereum are general (one can issue any kind of contract), distributed (an updated copy is present at all the nodes within the same network), shared (an arbitrary amount of contracts are served within the same infrastructure) and secure (there is no way to tamper with the stored data). All those properties are undeniably good, but the consequence of keeping all those promises is that the infrastructure is exceedingly complex. Such an extense architecture does not add any functionality to a smart contract, it makes it trustworthy.


    If one understands the raw concepts behind the Blockchain consensus, and we are willing to sacrifice some of the properties mentioned earlier, one can design and implement a simple ledger for smart contracts like pyledger (pyledger.readthedocs.io). Pyledger was designed as a platform for fast prototyping of smart contracts, and for experimentation, but in some particular cases can be good enough to be used in real-world cases.


    Finally... Fun time! All the concepts will be exemplified with a Q&A contest implemented as a smart contract where all attendants can play.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=eSaLdLrXzO4
- id: how-to-map-a-protein-structure-into-a-network-graph-to
  title: How to map a protein structure into a network graph to understand protein folding
  speakers:
  - massimo-domenico-sammito
  type: talk
  language: en
  description: 'In all living systems any biological function is carried out by the interactions of proteins. The specific function of a protein is determined by its own 3d shape that can be modeled in a list of single atom coordinates derived from experimental analysis. In our lab we use python to process the information of hundred thousands structures already known to predict common patterns in protein folding.


    **Abstract**


    From DNA, the genetic code is translated into proteins being these macro molecular structures in charge to execute specific cellular functions. All proteins are composed by the combination of the same 20 amino acids, indeed, it is the 3D shape and detailed structure that differentiate a protein from another and so their functions. Determining protein structure is fundamental to understand their biological function; modify and alter their structures is the way in which drugs can block or activate a protein activity and doing so preventing or treating diseases. In our lab we are understanding protein and DNA structures to the level of atomic resolution contributing to the biomedical research. We process with python the information of hundred thousands 3D coordinate structures already known and predict patterns that can be used to determine structure of unknown proteins. To achieve this objective, proteins are first reduced to a series of specific 3D vectors (Characteristic Vectors [#]_) and then the geometrical relationships among them are extracted. We make use of biopython and python-igraph libraries to model each structure vectors in a network graph and we use supervised and unsupervised learning to classify and predict structure features. Python-igraph is a wrapper to a C code implementation of a set of graph algorithms of classical use in network analysis.


    .. [#] Sammito M1, Millán C, Rodríguez DD, de Ilarduya IM, Meindl K, De Marino I, Petrillo G, Buey RM, de Pereda JM, Zeth K, Sheldrick GM, Usón I. Exploiting tertiary structure through local folds for crystallographic phasing. Nat Methods. 2013 Nov;10(11):1099-101. doi: 10.1038/nmeth.2644. Epub 2013 Sep 15.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=aEFR7_EzMJs
- id: python-for-visualization-of-hpc-applications
  title: Python for visualization of HPC applications
  speakers:
  - miguel-zavala-ake
  type: talk
  language: en
  description: This work describes the usage of python in application that makes use of high performance application (HPC). Such applications comprise examples as computational fluid dynamics, where the analysis of large data bases is necessary in order to extract useful information. On the other hand, a common way used in the analysis of data is the visualization. It can be done by libraries as matplotlib or pandas, however more sophisticated 3D visualization can also be performed though vtk and mpi4py libraries, or even though Blender of 3d Max. The two latter case enable the use of high quality rendering.
  links:
  - type: video
    url: https://www.youtube.com/watch?v=0ni90h8EErQ
- id: data-science-for-lazy-people-genetics-will-work-for-you
  title: Data science for lazy people... genetics will work for you!
  speakers:
  - diego-hueltes
  type: talk
  language: en
  description: 'Data science is fun... right? Data cleaning, feature selection, feature preprocessing, feature construction, model selection, parameter optimization, model validation... oh wait... are you sure? What about automating 80% of the work using genetic algorithms that can make better choices than you? TPOT is a tool that automatically creates and optimizes machine learning pipelines.


    **Abstract**


    We love Data Science, but sometimes we have to do some manual and repetitive work before starting with the interesting and fun parts, but that will change. TPOT is an open source tool built on top of scikit-learn for creating and optimizing machine learning pipelines. It can be considered a data science assistant. The library will automate from feature selection to parameter optimization, it is also able to do preprocessing or construct new features from existing ones. TPOT tests a huge number of pipelines to provide you with the optimal one, this work is done with genetic algorithms. It is easy to use, has a familiar syntax if you have used Pandas or scikit-learn, and it''s very powerful. Let genetics work for you!'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=-nTLS7BtcGA
  - type: slides
    url: https://slides.com/j-diegohueltesvega/data-science-lazy-people#/
- id: marketing-data-science
  title: Marketing Data Science
  speakers:
  - joaquin-pais
  type: talk
  language: en
  description: 'Marketing Data Science: how digital marketing needs data science to survive.


    **Abstract**


    Digital Marketing is changing the way corporations and brands communicates with customers. The investments in Digital Marketing are skyrocketing around the world in a multi-billion industry.


    But consumers and customers (specially millenials) does not trust advertising. Different approaches are being made by corporations like Inbound Marketing Strategies. My presentation is about how Digital Marketing needs Data Science in order to better understand the customer needs and generate new niches of interest for companies. Companies investing in Digital Marketing should take a close look at Data Science Platforms like Python in order to better gather inisghts, create segments and personalice a customer experience.


    I will provide some short examples about how we are using python jupyter notebook environment in order to gain inisghts from customers using IBM Watson API, generating new segmentation and customer experiences.'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=jzuQJg3bFy8
- id: using-network-community-clustering-algorithms-to-aid
  title: Using network community clustering algorithms to aid determination of protein structures
  speakers:
  - claudia-millan
  type: talk
  language: en
  description: 'How can you best exploit the information on the protein structures that we already know in order to solve the (many more) that we don''t know? That''s the question we try to solve in our group and this talk will show our use of community clustering on the use case of aiding protein structure solution.


    **Abstract**


    The study of proteins is extremely relevant to many fields, ranging from medicine to industrial processes. If a cell was a factory, proteins would be the workers, performing very specific tasks in a production chain, in which a failure at any of the steps might affect the others. In order to really understand the function of proteins, there are a number of biochemical techniques that we can apply, but to get a really accurate description of their mechanisms we need to have information up to their atomic level. Proteins are composed by different combinations of 20 amino acids which form chains and result in an intricate and functional structure. We know the final shape of the protein is dependent from its sequence but we can''t (currently) predict the outcome of a given sequence, so we need experimental techniques to obtain this information. We can''t directly look a protein with a microscope and see its three-dimensional atomic arrangement. There are biophysical techniques that allow us to get low-resolution shapes or surfaces of them, but the only current method that provides atomic detail is x-ray diffraction. In contrast to microscopy, were after illuminating your sample you can, with the appropriate lenses, transform back your reflected rays in an image, in x-ray diffraction we only get the Fourier transform of our protein''s structure, that is, its diffraction pattern, but we lose the phase information from the diffracted rays. This problem, known as the phase problem, is an issue in structure solution, because, compared to the intensities of the diffraction pattern, phases provide much more information about our protein''s structure. Phases can be computed from a coordinates model, so, if there is a structure of a protein that is expected to be similar (in terms of their coordinates) to an unknown one, it can be used to provide initial estimates of the phases and then improve them until the problem structure is solved.


    Proteins do not adopt random shapes. There are forces that act on them and, according to the chemical properties of the amino acids and the context they have around, they will arrange in particular forms. The first level of structure formed is what we call secondary structure, which is formed of alpha helices and beta strands. These are very general and are present in all kind of proteins. As letters in different books, which are general if looked at independently but can acquire a quite different meaning in ''El Quijote'' than in ''50 Shades of Grey'', these structure fragments alone have a different meaning than when set in a context with other structure elements. Yet, even combinations of a few elements can still be general and frequent, and have a sense, such as the phrase ''Once upon a time'' in so many tales. In the protein case, particular small combinations of alpha helices and beta strands should also appear more frequently and can be studied on their different contexts. In a way, we could say that, protein structures, from a top down view, look quite different between them, but from a bottom up one, when we go to small pieces, they look much more similar.


    In our group, we try to exploit these properties of protein structures for solving two types of problems. One is a search problem, consisting in understanding which is the best way in which to break down a larger model of a protein similar to an unknown one in order to refine it and get the correct phases and solve the structure. The other one is more of a prediction problem, in which we want to find structural units in the database of solved structures in order to help us interpret them and extract new information from this vast amount of data. In order to solve both problems we need a numerical description of our system than can help us describing its geometrical features in an accurate way. We have developed a description of such secondary structure fragments based on what we call characteristic vectors, that we also employ to represent the relations between such elements. This description can be implemented in a network graph that allows to use community clustering algorithms on it in order to evaluate simultaneously all the relations between the elements of the structure and find its communities.


    From the technical point of view, the language we use for our development is Python, and the tool in which our graphs are implemented is python-igraph. There are a number of community clustering algorithms available and deciding which is the best for our case and which metrics to use to describe our structures has been an interesting process that we want to share with you. In this talk I will explain our research and development on this topic and I will link the general descriptions to our current and successful use case, possibly leaving open questions on what can we do more!'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=9g-DaHZZKDE
  - type: slides
    url: https://drive.google.com/file/d/0Bzli2ZOV2beTd01ZdHBkWHc5b2M/view
- id: security-for-data-scientists
  title: Security for Data Scientists
  speakers:
  - david-arcos
  type: keynote
  language: en
  description: 'Handling confidential data attracts unwanted attention from hostile attackers.


    We will go over the basic concepts of security threats, show many examples of real attacks, and focus on how to defend ourselves and secure our data.


    Keep yourself safe!


    **Abstract**


    Main topics:


    * Myths

    * Why it''s important to be safe

    * Authentication & Password Managers

    * Phishing & 2FA

    * MITM & Encryption

    * Internet tracking & Ad-blockers

    * Internet Of Things

    * Physical Security

    * More Resources'
  links:
  - type: video
    url: https://www.youtube.com/watch?v=aicyYd8MZWo
  - type: slides
    url: https://www.slideshare.net/DZPM/security-for-data-scientists
- id: an-introduction-to-the-tidyverse
  title: An introduction to the tidyverse
  speakers:
  - jorge-cimentada
  type: talk
  links:
  - type: slides
    url: https://github.com/cimentadaj/PyData_2017
- id: introduction-to-data-analysis-with-pandas
  title: Introduction to data analysis with Pandas
  speakers:
  - eduard-goma
  type: talk
  links:
  - type: slides
    url: https://github.com/eduardgoma/pandas-workshop
- id: social-network-analysis-with-python-and-networkx
  title: Social Network Analysis with Python and NetworkX
  speakers:
  - jordi-torrents
  type: talk
  links:
  - type: slides
    url: https://github.com/jtorrents/pydata_bcn_NetworkX
photos:
  thread: https://x.com/PyBCN/status/865470914107891717
  items:
  - file: pydata-2017/01-first-day-of-pydatabcn-see-you-here.jpg
    caption: 'First day of #PyDataBCN See you here!'
    source: https://x.com/PyBCN/status/865470914107891717
    time: 09:35
  - file: pydata-2017/02-about-to-start-the-workshops-pydatabcn.jpg
    caption: 'About to start the workshops! #PyDataBCN'
    source: https://x.com/PyBCN/status/865471272750161920
    time: 09:36
  - file: pydata-2017/03-taking-numpy-in-stride-by-jaime-fernandez-del-rio.jpg
    caption: 'Taking NumPy in Stride, by Jaime Fernandez del Rio #PyDataBCN'
    source: https://x.com/PyBCN/status/865474452238155778
    time: 09:49
  - file: pydata-2017/04-introduction-to-data-analysis-with-pandas-is-full.jpg
    caption: Introduction to data analysis with Pandas is full! With Eduard Goma
    source: https://x.com/PyBCN/status/865474697214836736
    time: 09:50
    talk: introduction-to-data-analysis-with-pandas
  - file: pydata-2017/05-an-introduction-to-the-tidyverse-by-jorge-cimentad.jpg
    caption: 'An introduction to the tidyverse, by Jorge Cimentada #PyDataBCN'
    source: https://x.com/PyBCN/status/865510553984286722
    time: '12:12'
    talk: an-introduction-to-the-tidyverse
  - file: pydata-2017/06-waves-hackaton-by-mcarricano-pydatabcn.jpg
    caption: 'Waves hackaton, by @mcarricano #PyDataBCN'
    source: https://x.com/PyBCN/status/865511932362539010
    time: '12:18'
  - file: pydata-2017/07-high-performance-python-for-data-analysis-by-guill.jpg
    caption: 'High Performance Python for Data Analysis, by @guillemborrell #PyDataBCN'
    source: https://x.com/PyBCN/status/865517539853344768
    time: '12:40'
  - file: pydata-2017/08-hdf5-and-pandas-by-francescalted-pydatabcn.jpg
    caption: 'HDF5 and pandas, by @FrancescAlted #PyDataBCN'
    source: https://x.com/PyBCN/status/865564323120283648
    time: '15:46'
  - file: pydata-2017/09-social-network-analysis-with-python-and-networkx-b.jpg
    caption: 'Social Network Analysis with Python and NetworkX, by Jordi Torrents #PyDataBCN'
    source: https://x.com/PyBCN/status/865564663748194305
    time: '15:47'
    talk: social-network-analysis-with-python-and-networkx
  - file: pydata-2017/10-good-morning-today-we-ll-have-lightning-talks-go-t.jpg
    caption: 'Good Morning! Today we''ll have Lightning Talks, go to the board and write down your proposal! First come, first served :) #PyDataBCN'
    source: https://x.com/PyBCN/status/865816252920549377
    time: 08:27
  - file: pydata-2017/11-welcome-to-pydatabcn-2017.jpg
    caption: 'Welcome to #PyDataBCN 2017!'
    source: https://x.com/PyBCN/status/865829255829213184
    time: 09:19
  - file: pydata-2017/12-ifosch-our-great-sponsors-made-pydatabcn-possible.jpg
    caption: 'Our great sponsors made #PyDataBCN possible, thank you all!'
    source: https://x.com/PyBCN/status/865831488297762816
    time: 09:28
  - file: pydata-2017/13-first-keynote-data-science-and-machine-learning-wi.jpg
    caption: 'First Keynote: Data science and Machine Learning with Anaconda, by @teoliphant from @ContinuumIO #PyDataBCN'
    source: https://x.com/PyBCN/status/865832295533510656
    time: 09:31
  - file: pydata-2017/14-pydatabcn-keynote-speaker-teoliphant-is-on-stage-t.jpg
    caption: '#PyDataBCN keynote speaker @teoliphant is on stage talking about data science stack and software tools!'
    source: https://x.com/PyBCN/status/865835722003156992
    time: 09:44
  - file: pydata-2017/15-second-keynote-the-magic-behind-pyspark-how-it-imp.jpg
    caption: 'Second Keynote: The Magic Behind PySpark, how it impacts perf & the "future", by @holdenkarau from @IBM #PyDataBCN'
    source: https://x.com/PyBCN/status/865849763849285632
    time: '10:40'
    talk: the-magic-behind-pyspark-how-it-impacts-perf-the-future
  - file: pydata-2017/16-third-keynote-nasa-space-apps-challenge-asteroid-p.jpg
    caption: 'Third Keynote: NASA Space APPS Challenge: Asteroid prediction impact, by @SoyGema #PyDataBCN #TensorFlow'
    source: https://x.com/PyBCN/status/865947122696409088
    time: '17:07'
    talk: nasa-space-apps-challenge-asteroid-prediction-impact
  - file: pydata-2017/17-fourth-keynote-squeeze-gently-your-big-data-by-fra.jpg
    caption: 'Fourth Keynote: Squeeze (Gently) Your (Big) Data, by @FrancescAlted #PyDataBCN'
    source: https://x.com/PyBCN/status/866215737270173696
    time: '10:54'
  - file: pydata-2017/18-lightning-talks-pydatabcn.jpg
    caption: 'Lightning Talks! #PyDataBCN'
    source: https://x.com/PyBCN/status/866308840140279808
    time: '17:04'
  - file: pydata-2017/19-last-keynote-closing-act-security-for-data-scienti.jpg
    caption: 'Last Keynote, Closing Act: Security for Data Scientists, by @DZPM from @LeadRatings #PyDataBCN'
    source: https://x.com/PyBCN/status/866327528121741313
    time: '18:19'
    talk: security-for-data-scientists
  album: https://www.flickr.com/photos/pydata/sets/72157684439580266/
---

The [PyData 2017 - Barcelona edition](https://pydata.org/barcelona2017/) took place from May 19th to 21th at [ESADE](https://www.esade.edu/homesite/esp/esadeforum). The talks below link to the page of each one, with its video and its slides. The event also published an album of [photos](https://www.flickr.com/photos/pydata/sets/72157684439580266/) and a playlist of its [videos](https://www.youtube.com/playlist?list=PLGVZCDnMOq0oieXy92cJBwSirA3G2MCU1).
