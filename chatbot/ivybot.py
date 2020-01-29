from nltk.chat.util import Chat, reflections
#Pairs is a list of patterns and responses.
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"(hi|Is anyone there?|Hello|Whats up|Hi|hello|Hey|hey)(.*)",
        ["Hello!", "Good to see you again!","Hi there, how can I help?"]
    ],
    [
        r"(Bye|See you later|Goodbye|I am leaving|Have a good day|Have a nice day|Bye|bye)(.*)",
        ["Sad to see you go :(",
                 "Talk to you later",
                 "Goodbye!"]
    ],
    [
        r"(What is Blue economy?|What does Blue economy stand for?|What does Blue economy mean?)(.*)",
        ["Blue economy is a term in economics relating to the exploitation and preservation of the marine environment.",
                 "The Blue Economy is an economic arena that depends on the benefits and values realized from the coastal and marine environment.",
                 "According to the World Bank, the blue economy can be described as 'sustainable use of ocean resources for economic growth, improved livelihoods and jobs while preserving the health of ocean ecosystem'",
                 "The Commonwealth of Nations considers it as “an emerging concept which encourages better stewardship of our ocean or ‘’blue” resources",
                 "The Center for the Blue Economy says than now it is a widely used term around the world with three related but distinct meanings- the overall contribution of the oceans to economies, the need to address the environmental and ecological sustainability of the oceans, and the ocean economy as a growth opportunity for both developed and developing countries."]
    ],
    [
        r"(What is Blue economy related to?|What terms is it related to?|What terms is Blue economy related to?|What terms is it related to?)(.*)",
        ["Blue economy is related to the terms Ocean economy, Green economy and Blue growth.",
                 "Terms related to Blue economy are Ocean economy, Green economy and Blue growth.",
                 "Important relations to Blue economy are the terms Ocean economy, Green economy and Blue growth."]
    ],
    [
        r"(What is Ocean economy?|What does Ocean economy mean?|What is the meaning of the term 'Ocean economy'?)(.*)",
        ["Ocean economy simply deals with the use of ocean resources and is strictly aimed at empowering the economic system of ocean."]
    ],
    [
        r"(What is Green economy?|What does Green economy mean?|What is the meaning of 'Green economy?|What is the meaning of the term 'Green economy'?)(.*)",
        ["The green economy is defined as an economy that aims at reducing environmental risks.",
                 "Green economy  aims for sustainable development without degrading the environment."]
    ],
    [
        r"(What is Blue growth?|What does Blue growth mean?|What is the meaning of the term 'Blue growth'?)(.*)",
        [ "Blue growth means 'support to the growth of the maritime sector in a sustainable way'"]
    ],
    [
        r"(What challenges does Blue economy deal with?|What gets in the way of Blue economy?)(.*)",
        [ "Current economic trends that have been rapidly degrading ocean resources.",
                 "The lack of investment in human capital for employment and development in innovative blue economy sectors.",
                 "Inadequate care for marine resources and ecosystem services of the oceans."]
    ],
    [
        r"(Which sectors does Blue economy affect?|Which sectors are connected to Blue economy?|Which sectors does it affect?|Which sectors get affected by Blue economy?)(.*)",
        [  "Some of the sectors it affects are Aquaculture, Maritime biotechnology and Fishing",
                 "Some of the sectors it affects are Maritime transport, Coastal protection and Waste disposal",
                 "Some of the sectors affected by the Blue economy are Maritime and coastal tourism and Mineral resources"]
    ],
    [
        r"(Which companies support the Blue economy?|Which companies is Blue economy supported by?|What companies support Blue economy?)(.*)",
        ["Some of the companies that support the Blue economy are Scotrenewables Tidal Resources Ltd., Atlantis Resources Ltd. and Wavestar Energy ",
                 "Some companies supporting Blue economy are Carnegie Wave, Siemens Wind Power and Marine Harvest",
                 "The World Bank is deeply committed to supporting the blue economy, with a blue portfolio of USD 2.6 billion in investments.",
                 "Some of the companies supporting the Blue economy are PharmaMar, Stellar Biotechnologies and Porifarma"]
    ],
    [
        r"(What does Blue economy help with?|what does Blue economy help with?|what does blue economy help with|What good does Blue economy do?|What does Blue economy provide?)(.*)",
        ["The blue economy provides food, jobs, water, and is a source of economic growth.",
                 "It provides the livelihood for hundreds of millions of the poorest and most vulnerable people in the world.",
                 "By one estimate, it generates USD 3-6 trillion to the world economy."]
    ],
    [
        r"(Why is Blue economy important?|Why is the Blue economy important?)(.*)",
        ["The ocean is fundamental to life on Earth covering nearly three quarters of our planet. It produces more than half the oxygen that we breathe yet our oceans are moving deeper into ecological crisis just at the moment when we need them more than ever so we should try to help them."]
    ],
]

#A Function to run the chatbot
def ivy():
  print("Hi, I'm Ivy and I want to help and chat with you! \nPlease type 'Hello' start a conversation. Type quit to leave ") #default message at the start
  chat = Chat(pairs,reflections)
  chat.converse()
#Run the chatbot
ivy()
