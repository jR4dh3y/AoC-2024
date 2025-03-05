var list1 = new List<int>();
var list2 = new List<int>();

var lines = File.ReadAllLines("inputs.txt");

foreach (var line in lines)
{
    var parts = line.Split(' ', StringSplitOptions.RemoveEmptyEntries);

    if (int.TryParse(parts[0], out var number))
    {
        list1.Add(number);
    }
    if (int.TryParse(parts[1], out number))
    {
        list2.Add(number);
    }
}

list1.Sort();
list2.Sort();

var totaldiff = 0;
for (int i = 0; i < list1.Count; i++)
{
    totaldiff += Math.Abs(list1[i] - list2[i]);
}

Console.WriteLine(totaldiff);
Console.ReadKey();
list1 = []
list2 = []

with open("inputs.txt") as file:
    lines = file.readlines()

for line in lines:
    parts = line.split()

    try:
        list1.append(int(parts[0]))
    except ValueError:
        pass

    try:
        list2.append(int(parts[1]))
    except ValueError:
        pass

list1.sort()
list2.sort()

totaldiff = 0
for i in range(len(list1)):
    totaldiff += abs(list1[i] - list2[i])

print(totaldiff)