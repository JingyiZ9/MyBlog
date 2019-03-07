---
layout: post
title:  "C# nullabls"
---
What's the mearning of C#'s nullables?
For primitive types, like *int*, *bool*, *decimal*, *double* in C#, they cannot be null, while Reference types like *object*, *dynamic* can point to null(like `string something = null`). So C# have created a wrapper type nullable such that primitive types can be able to point to Nullable values. And this characteristic would be most useful for databases.
