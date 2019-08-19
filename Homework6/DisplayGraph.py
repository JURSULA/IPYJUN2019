from tkinter import *
class DisplayGraph:
    def __init__(self, filename):
        self.__filename = filename

    def toDisplayGraph(self):
        graphData = ""
        vertices = []
        edges = []
        v_dict = {}
        numOfVertices = 0
        with open(self.__filename, "r") as work_file:
            numOfVertices = int(work_file.readline())
            graphData = work_file.readlines()
            #print(numOfVertices)
        #print(graphData)
        for i in range(numOfVertices):
            verticeData = graphData[i].strip().split()
            v = [verticeData[0], verticeData[1], verticeData[2]]
            v_dict[verticeData[0]] = [verticeData[1], verticeData[2]]
            #print(verticeData)
            #print(v)
            vertices.append(v)
            for j in range(3, len(verticeData)):
                e = [verticeData[0],verticeData[j]]
                edges.append(e)
        #print(edges)
        #print(vertices)
        print(v_dict)
        window = Tk()
        window.title("Display a Graph")
        window.geometry("500x500")

        frame = Frame(window)
        frame.pack()

        canvas = Canvas(frame, width = 300, height = 200)
        canvas.pack()
        radius = 3
        for verticeName, x, y in vertices:
            x = int(x)
            y = int(y)
            canvas.create_text(x - 2 * radius, y - 2 * radius, text= verticeName, tags="graph")
            canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="black", tags="graph")
        for startEdge, endEdge in edges:
            arr1= v_dict[startEdge]
            arr2 = v_dict[endEdge]
            '''startEdge = int(startEdge)
            endEdge = int(endEdge)
            canvas.create_line(vertices[startEdge][1], vertices[startEdge][2], vertices[endEdge][1], vertices[endEdge][2], tags="graph")'''
            canvas.create_line(arr1[0], arr1[1],arr2[0],arr2[1], tags="graph")
        window.mainloop()










