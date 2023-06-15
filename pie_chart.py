import matplotlib.pyplot as plt
import numpy as np

def plot_pie():
    news_source_data = ["Limited vaccine availability","Vaccine hesitancy or fear of side effects","Limited vaccine availability","Limited vaccine availability","Vaccine hesitancy or fear of side effects","Vaccine hesitancy or fear of side effects","Limited vaccine availability","Limited vaccine availability","Limited vaccine availability","Limited vaccine availability","Vaccine hesitancy or fear of side effects","Vaccine hesitancy or fear of side effects","Vaccine hesitancy or fear of side effects","Vaccine hesitancy or fear of side effects","Vaccine hesitancy or fear of side effects","Limited vaccine availability","Vaccine hesitancy or fear of side effects","Limited vaccine availability","Vaccine hesitancy or fear of side effects","Vaccine hesitancy or fear of side effects","Vaccine hesitancy or fear of side effects","Limited vaccine availability","Inaccessible vaccination centers","Lack of information or misinformation","Vaccine hesitancy or fear of side effects","Vaccine hesitancy or fear of side effects","Inaccessible vaccination centers","Lack of information or misinformation","Vaccine hesitancy or fear of side effects","Vaccine hesitancy or fear of side effects","Vaccine hesitancy or fear of side effects","Limited vaccine availability, Inaccessible vaccination centers, Lack of information or misinformation, Vaccine hesitancy or fear of side effects","Vaccine hesitancy or fear of side effects","Inaccessible vaccination centers, Lack of information or misinformation, Vaccine hesitancy or fear of side effects","Vaccine hesitancy or fear of side effects","Vaccine hesitancy or fear of side effects","Limited vaccine availability, Inaccessible vaccination centers","Vaccine hesitancy or fear of side effects","Vaccine hesitancy or fear of side effects","Inaccessible vaccination centers, Vaccine hesitancy or fear of side effects","Vaccine hesitancy or fear of side effects","Vaccine hesitancy or fear of side effects","Vaccine hesitancy or fear of side effects"]

    availability=fear=centers=lackInfo = 0
    for source in news_source_data:
        if "Limited vaccine availability" in source:
            availability=availability+1
        if "Vaccine hesitancy or fear of side effects" in source:
            fear=fear+1
        if "Inaccessible vaccination centers" in source:
            centers=centers+1
        if "Lack of information or misinformation" in source:
            lackInfo=lackInfo+1
            
    print(availability)
    print(fear)
    print(centers)
    print(lackInfo)
    source = [availability,fear,centers,lackInfo]
    source_label = ["Limited vaccine availability","Vaccine hesitancy or fear of side effects","Inaccessible vaccination centers","Lack of information or misinformation"]
    explode = (0.05, 0.1, 0.05, 0.05)

    plt.pie(source, colors=["#2c97f5","#97ff6b","#ff6961","orange"],labels = source_label,autopct='%1.0f%%',pctdistance=0.82,explode=explode)
    centre_circle = plt.Circle((0, 0), 0.7, fc='white')
    fig = plt.gcf()
    # Adding Circle in Pie chart
    fig.gca().add_artist(centre_circle)
    plt.title('Reasons for not taking vaccine', weight='bold',font='Comic Sans MS',size=20)
    return plt