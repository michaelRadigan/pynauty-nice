# pynauty

A pynauty fork in an effort to ease installation. Pynauty is a python wrapper around nauty, distributed under the GNU GPLv3. Nauty is an isomorphism finder, written in C, distributed under the APACHE 2.0 licence. Previously, the two would have to be dowloaded separately from their respective websites, unpacked, built and symbolically linked. Given that that in this direction the licences are compatible and allow it, I've decided to redistribute them together. 

Note that this isn't quite finished but is sufficient for my use case, if you would like me to change or improve anything then please let me know.

# Initial pynauty licence

Copyright (c) 2015 Peter Dobsan

pynauty is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.

# Initial nauty  (and traces) licence

This is the license for the software package Nauty and
Traces, package versions 2.6r3 and later.

Five categories of software are included in the package:
A. All files not listed as B-E below, copyright Brendan McKay (1984-)
B. Files traces.h, traces.c and dretodot.c, copyright Adolfo Piperno (2008-)
C. File watercluster2.c, copyright Gunnar Brinkmann (2009-)
D. Files planarity.h and planarity.c, copyright Magma project.
E. Files nautycliquer.h and nautycliquer.c, copyright to Sampo
   Niskanen and Patric Ã–stergÃ¥rd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this software except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Brendan McKay: Australian National University; Brendan.McKay@anu.edu.au
Adolfo Piperno: University of Rome "Sapienza"; piperno@di.uniroma1.it
Gunnar Brinkmann: University of Ghent; Gunnar.Brinkmann@UGent.be
Magma Administration: University of Sydney; admin@maths.usyd.edu.au
Patric Ostergard: Aalto Univerity; patric.ostergard@aalto.fi

---END-OF-FORMAL-COPYRIGHT-NOTICE---

Earlier (pre-2.6) versions of this package carried a different
notice: "Permission is hereby given for use and/or distribution
with the exception of sale for profit or application with nontrivial
military significance." These days most people use nauty via a
larger package such as Magma, Sage, or GAP, and often they don't
even know they are using nauty. Due to the legal nonsense that
large package distributors need to worry about, it has proved too
much trouble to maintain an idiosyncratic licence. I didn't change
my opinion about military use, but it is no longer part of the
formal notice. Brendan McKay (Jan 20, 2016)