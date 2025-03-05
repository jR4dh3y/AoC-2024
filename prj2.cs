var list1 = new List<int>();
var list2 = new List<int>();

var lines = File.ReadAllLines("inputs.txt");

var counts1 = new Dictionary<int, int>();
var counts2 = new Dictionary<int, int>();


foreach (var line in lines)
{
    var parts = line.Split(' ', StringSplitOptions.RemoveEmptyEntries);

    if (int.TryParse(parts[0], out var number))
    {
        list1.Add(number);
        if (counts1.ContainsKey(number))
        {
            counts1[number]++;
        }
        else
        {
            counts1[number] = 1;
        }
    }
    if (int.TryParse(parts[1], out number))
    {
        list2.Add(number);
        if (counts2.ContainsKey(number))
        {
            counts2[number]++;
        }
        else
        {
            counts2[number] = 1;
        }
    }
}



var total = 0;
foreach ( var item in counts1)
{
    if (counts2.ContainsKey(item.Key))
    {
        total += item.Value * counts2[item.Key];
    }
}

Console.WriteLine(total);
Console.ReadKey();