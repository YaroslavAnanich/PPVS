#include "pch.h"
#include "CppUnitTest.h"
#include "..\lab_1\BST.h"
using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace lab1tests
{
	TEST_CLASS(lab1tests)
	{
	public:
		
		TEST_METHOD(Test_Get_Size)
		{
			BST tree;
			tree.push("wolf", "volk");
			Assert::IsTrue(tree.getSize() == 1);
		}
		TEST_METHOD(Test_Operator)
		{
			BST tree;
			tree.push("wolf", "volk");
			Assert::IsTrue(tree["wolf"] == "volk");
		}
		TEST_METHOD(Test_Del)
		{
			BST tree;
			tree.push("wolf", "volk");
			tree.push("table", "stol");
			tree.del("table", "stol");
			Assert::IsTrue(tree.getSize() == 1);
		}
		TEST_METHOD(Negative_Test_Del)
		{
			BST tree;
			tree.push("wolf", "volk");
			tree.push("table", "stol");
			tree.del("cool", "stol");
			Assert::IsTrue(tree.getSize() == 2);
		}
		TEST_METHOD(Test_Change_Translation)
		{
			BST tree;
			tree.push("wolf", "volk");
			tree.change_translation("wolf", "dom");
			Assert::IsTrue(tree["wolf"] == "dom");
		}
		TEST_METHOD(Negative_Test_Change_Translation)
		{
			BST tree;
			tree.push("wolf", "volk");
			tree.change_translation("home", "dom");
			Assert::IsTrue(tree["wolf"] == "volk");
		}
		TEST_METHOD(Negative_Test_Pull_File)
		{
			BST tree;
			tree.pull_file("file.txt");
			Assert::IsTrue(tree.getSize() == 0);
		}
	};
}
