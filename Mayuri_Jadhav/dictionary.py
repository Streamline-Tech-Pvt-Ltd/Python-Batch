# Python Dictionary

## What is a Dictionary?

A **Dictionary** stores data in **key-value pairs**.


student = {
    "name": "Mayuri",
    "age": 22,
    "city": "Pune"
}

print(student)


**Output:**

{'name': 'Mayuri', 'age': 22, 'city': 'Pune'}


## Dictionary Rules

* Uses `{}`.
* Stores data as `key: value`.
* Keys must be **unique**.
* Keys must be **immutable**.
* Values can be duplicated.
* Dictionary is **mutable**.
* Maintains insertion order.


# Dictionary Methods

## 1. `keys()`

Returns all keys.


student = {"name": "Mayuri", "age": 22}

print(student.keys())


**Output:**


dict_keys(['name', 'age'])



## 2. `values()`

Returns all values.



student = {"name": "Mayuri", "age": 22}

print(student.values())


**Output:**


dict_values(['Mayuri', 22])







## 3. `items()`

Returns all key-value pairs.



student = {"name": "Mayuri", "age": 22}

print(student.items())


**Output:**


dict_items([('name', 'Mayuri'), ('age', 22)])


## 4. `get()`

Returns the value of a key.



student = {"name": "Mayuri", "age": 22}

print(student.get("name"))


**Output:**


Mayuri



## 5. `update()`

Adds or updates data.



student = {"name": "Mayuri", "age": 22}

student.update({"city": "Pune"})

print(student)


**Output:**


{'name': 'Mayuri', 'age': 22, 'city': 'Pune'}

## 6. `copy()`

Creates a copy of the dictionary.



student = {"name": "Mayuri", "age": 22}

student2 = student.copy()

print(student2)


**Output:**


{'name': 'Mayuri', 'age': 22}


## 7. `pop()`

Removes a specific key.



student = {"name": "Mayuri", "age": 22}

student.pop("age")

print(student)


**Output:**


{'name': 'Mayuri'}


## 8. `popitem()`

Removes the last key-value pair.



student = {
    "name": "Mayuri",
    "age": 22,
    "city": "Pune"
}

student.popitem()

print(student)


**Output:**


{'name': 'Mayuri', 'age': 22}


## 9. `setdefault()`

Returns the value if the key exists.
If the key does not exist, it adds the key.



student = {"name": "Mayuri", "age": 22}

student.setdefault("city", "Pune")

print(student)


**Output:**


{'name': 'Mayuri', 'age': 22, 'city': 'Pune'}


## 10. `clear()`

Removes all items.



student = {"name": "Mayuri", "age": 22}

student.clear()

print(student)


**Output:**


{}


## 11. `fromkeys()`

Creates a new dictionary using given keys.



keys = ["name", "age", "city"]

student = dict.fromkeys(keys)

print(student)


**Output:**


{'name': None, 'age': None, 'city': None}


### With Default Value



keys = ["name", "age", "city"]

student = dict.fromkeys(keys, "Unknown")

print(student)


**Output:**


{'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}


# Quick Revision

| Method         | Use                         |
|
 |
| `keys()`       | Get all keys                |
| `values()`     | Get all values              |
| `items()`      | Get key + value             |
| `get()`        | Get value                   |
| `update()`     | Add / Update                |
| `copy()`       | Copy dictionary             |
| `pop()`        | Delete specific key         |
| `popitem()`    | Delete last item            |
| `setdefault()` | Add if key doesn't exist    |
| `clear()`      | Delete all items            |
| `fromkeys()`   | Create dictionary from keys |
