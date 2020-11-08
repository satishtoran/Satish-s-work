{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 106,
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
      "Add a new name:Golu\n",
      "('Satish', 'Alok', 'Program') Golu\n",
      "(('Satish', 'Alok', 'Program'), 'Golu')\n"
     ]
    }
   ],
   "source": [
    "data2 = ('Satish','Alok','Program')\n",
    "print(len(data2))\n",
    "for x in range (len(data2)):\n",
    "    print (data2[x])\n",
    "p = input ('Add a new name:' )\n",
    "print (data2,p)\n",
    "\n",
    "data2 = data2, p\n",
    "print (data2)"
   ]
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
