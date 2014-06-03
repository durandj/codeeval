#include <fstream>
#include <iostream>
#include <string>
#include <cstring>

#define bit(x, p) ((x & 1 << (p - 1)) >> (p - 1))

int main(int argc, char **argv)
{
	if (argc == 1)
	{
		std::cout << "No input file given" << std::endl;
		return 0;
	}

	std::ifstream fsInput(argv[1]);
	fsInput >> std::ws;

	std::string sLine;
	while (getline(fsInput, sLine))
	{
		if (sLine.empty())
			continue;

		int x, p0, p1;
		sscanf(sLine.c_str(), "%d,%d,%d", &x, &p0, &p1);

		if (bit(x, p0) == bit(x, p1))
			std::cout << "true" << std::endl;
		else
			std::cout << "false" << std::endl;
	}

	fsInput.close();

	return 0;
}

