from rest_framework import serializers
from .models import StaffBase, Manager, Intern, Address


class StaffBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffBase
        fields = '_all_'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '_all_'



class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '_all_'
        has_company_card = Manager



class InternSerializer(serializers.ModelSerializer):
    StaffBase = StaffBaseSerializer()
    Manager = ManagerSerializer()

    class Meta:
        model = Intern
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'dob',
            'email',
            'phone_number',
            'StaffBase',
            'Manager',
        ]

    def create(self, validated_data):
        StaffBase_data = validated_data.pop('StaffBase')
        Manager_data = validated_data.pop('Manager')

        staffBase = StaffBase.objects.create(**StaffBase_data)
        Manager = Manager.objects.create(**Manager_data)

        user = Intern.objects.create(StaffBase=StaffBase, Manager=Manager, **validated_data)
        return user

    def update(self, instance, validated_data):
        StaffBase_data = validated_data.pop('StaffBase', None)
        Manager_data = validated_data.pop('Manager', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if StaffBase_data:
            for attr, value in StaffBase_data.items():
                setattr(instance.StaffBase, attr, value)
            instance.StaffBase.save()

        if Manager_data:
            for attr, value in Manager_data.items():
                setattr(instance.Manager, attr, value)
            instance.Manager.save()

        return instance


class CompanyProfileSerializer(serializers.ModelSerializer):
    company_StaffBase = StaffBaseSerializer()

    class Meta:
        model = Intern
        fields = '_all_'

    def create(self, validated_data):
        StaffBase_data = validated_data.pop('company_StaffBase')
        StaffBase = StaffBase.objects.create(**StaffBase_data)
        company = StaffBase.objects.create(company_StaffBase=StaffBase, **validated_data)
        return company

    def update(self, instance, validated_data):
        StaffBase_data = validated_data.pop('company_StaffBase', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if StaffBase_data:
            for attr, value in StaffBase_data.items():
                setattr(instance.company_StaffBase, attr, value)
            instance.company_StaffBase.save()

        return instance