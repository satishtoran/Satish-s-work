{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "Satish\n",
      "Alok\n",
      "Program\n",
      "Golu\n",
      "Molu\n",
      "Tolu\n",
      "Polu\n",
      "Bholu\n",
      "Putolu\n",
      "!END\n",
      "((((((('Satish', 'Alok', 'Program'), 'Golu'), 'Molu'), 'Tolu'), 'Polu'), 'Bholu'), 'Putolu')\n"
     ]
    }
   ],
   "source": [
    "data2 = ('Satish','Alok','Program')\n",
    "print(len(data2))\n",
    "\n",
    "for x in range (len(data2)):\n",
    "    print (data2[x])\n",
    "\n",
    "p='START'    \n",
    "while p != '!END' : #True\n",
    "    p=input()\n",
    "    if p != '!END': #Ture\n",
    "        data2 = data2,p\n",
    "    else:\n",
    "        break\n",
    "    \n",
    "print (data2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
